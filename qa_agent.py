from langchain.llms import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
import pickle
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = API_KEY


class SingleQaAgent():
    def __init__(self, vectorstore_path, temperature=0.5, num_docs_to_retrieve=6):
        self.db = self.init_db(vectorstore_path)
        self.retriever = self.db.as_retriever(
            search_kwargs={"k": num_docs_to_retrieve})

        self.chain = load_qa_with_sources_chain(
            OpenAI(temperature=temperature), chain_type="stuff")

        self.history = []

    def init_db(self, vectorstore_path):
        with open(vectorstore_path, "rb") as f:
            return pickle.load(f)

    def ask(self, query, return_only_outputs=True):
        docs = self.retriever.get_relevant_documents(query)

        res = self.chain({"input_documents": docs, "question": query},
                         return_only_outputs=return_only_outputs)

        self.history.append((query, res))

        # print(f"[USER]: {res['question']}")
        print(f"[PenDragon]: {res['output_text']}\n")

        if not return_only_outputs:
            print("[Passages Consulted]:")
            for idx, source in enumerate(res["input_documents"]):
                print(f"--- [{idx+1}] {source.page_content}")

        return res


if __name__ == "__main__":
    # Run the QA agent in interactive mode
    agent = SingleQaAgent("./db_cs_with_sources.pkl",
                          temperature=0.5, num_docs_to_retrieve=6)

    while True:
        query = input("> ")
        agent.ask(query)  # return_only_outputs=False
