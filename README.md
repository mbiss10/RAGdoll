# RAGdoll

A RAG model for conversational course reccomendations.

![ragdoll_poster_final](https://github.com/mbiss10/RAGdoll/assets/50077908/a9f86c98-3287-42af-a285-5e8de9999517)

### Repository Overview:
- `data` stores our input copora, questions, and reference answers to evaluate our model. The dev set is based on the CSCI department and the test set is based on the MATH department. 
- `evaluation` stores all the files used to evaluate our model. It contains a `human_scores` directory, which contains human evaluation of the model's correctness. Additionally, it contains an `output` repo, which contains auto-generated files containing the results of our evaluation using the ROUGE and BLEU metrics. Finally, it conatains `evaluate.py`, a script responsible for generating the files in output.
- `results` stores the results of each model run. It contains both a plain text and pickled representation of the model's history (i.e. the questions it was asked, its responses to said questions, and the sources it consulted to answer each question.
- `process_data.py` takes as input a set of JSON objects for each course in `data/courses.json` and a manually curated plain text file representing major information. It produces a pickled vector store using OpenAI embeddings to embed each entry and FAISS to quickly complete similarity search and produce a vector store.
- `single_qa_agent.py` contains the `SingleQAAgent` class, which implements chatbot functionality. The user is prompted for an input and the RAG model generates output using the  RAG model.



### Other Notes:

- Uses `Python 3.8.16`
- Requires an OpenAI key, which is expected in a `.env` file. 
- Leverages [LangChain](https://blog.langchain.dev/) for model infrastructure.
