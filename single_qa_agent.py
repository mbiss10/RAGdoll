from langchain.llms import OpenAI
from langchain.retrievers import TFIDFRetriever
from langchain.schema import Document
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
import pickle
import os
import prompts as prompts
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = API_KEY


class SingleQaAgent():
    def __init__(self,
                 vectorstore_path,
                 model_name,
                 temperature=0.5,
                 vectorstore_k=6,
                 passages_path=None,
                 tfidf_k=6,
                 prompt=None
                 ):
        self.db = self.init_db(vectorstore_path)
        self.vectorstore_retriever = self.db.as_retriever(
            search_kwargs={"k": vectorstore_k})

        self.tfidf_retriever = None
        if passages_path is not None:
            self.tfidf_retriever = self.init_tfidf_retriever(
                passages_path, tfidf_k)

        if prompt is not None:
            self.chain = load_qa_with_sources_chain(
                OpenAI(model_name=model_name, temperature=temperature), chain_type="stuff", prompt=prompt)
        else:
            self.chain = load_qa_with_sources_chain(
                OpenAI(model_name=model_name, temperature=temperature), chain_type="stuff")

        self.history = []

    def init_db(self, vectorstore_path):
        with open(vectorstore_path, "rb") as f:
            return pickle.load(f)

    def init_tfidf_retriever(self, passages_path, tfidf_k):
        data = None
        with open(passages_path, "rb") as f:
            data = pickle.load(f)

        texts, sources = list(zip(*data))

        res = TFIDFRetriever.from_texts(texts, k=tfidf_k)
        res.docs = [Document(page_content=t, metadata={"source": s})
                    for t, s in zip(texts, sources)]
        return res

    def ask(self, query, return_only_outputs=True):
        docs = self.vectorstore_retriever.get_relevant_documents(query)

        if self.tfidf_retriever is not None:
            tf_idf_docs = self.tfidf_retriever.get_relevant_documents(query)
            docs.extend(tf_idf_docs)

        res = self.chain({"input_documents": docs, "question": query},
                         return_only_outputs=return_only_outputs)

        self.history.append((query, res))

        # print(f"[USER]: {res['question']}")
        print(f"[RAGDoll]: {res['output_text']}\n")

        if not return_only_outputs:
            print("[Passages Consulted]:")
            for idx, source in enumerate(res["input_documents"]):
                print(f"--- [{idx+1}] {source.page_content}")

        return res


if __name__ == "__main__":
    # Run the QA agent in interactive mode
    agent = SingleQaAgent("./data/dev/db_cs_with_sources.pkl",
                          model_name="gpt-3.5-turbo",
                          temperature=0.2,
                          vectorstore_k=8,
                          prompt=prompts.TURBO_PROMPT,
                          passages_path="./data/dev/cs_data.pkl",
                          tfidf_k=10)

    while True:
        query = input("> ")
        agent.ask(query, return_only_outputs=False)
