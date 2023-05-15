# RAGdoll

A RAG model for conversational course reccomendations.


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


# Example Results:
## 😀 The Good
Inference (e.g. recognizing "language" to mean programming language... and this snippet was buried deep within the CS 331 course description):  
<img width="479" alt="Screenshot 2023-05-15 at 2 56 11 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/dd08a671-d906-4155-994b-775d8e0ed234">  

Avoiding hallucinations:  
<img width="320" alt="Screenshot 2023-05-15 at 2 55 56 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/dcfa1175-7d55-484d-aa37-03406fe0a516">
<img width="320" alt="Screenshot 2023-05-15 at 2 55 53 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/a57356f4-7079-42ef-9d74-bc780400b7f2">
<img width="320" alt="Screenshot 2023-05-15 at 2 55 59 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/46ecf015-f78d-4324-82fb-818be9231c9a">  

General reasoning:  
<img width="576" alt="Screenshot 2023-05-15 at 2 55 31 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/b596429d-e79e-4afe-98c0-0ca05197940f">  

Temporal comparisons (there are two sections of Deep Learning, so it needed to recognize that one preceeds the other):  
<img width="409" alt="Screenshot 2023-05-15 at 2 55 42 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/4533baaf-c60b-4192-9be3-c837e6bcfcfa">  

Fun generative behavior:  
<img width="764" alt="Screenshot 2023-05-15 at 3 08 33 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/d08bb548-f3d0-40de-88be-9b6aed41f349">

## 🤨 The Not So Good
Trouble with basic arithmetic:  
<img width="901" alt="Screenshot 2023-05-15 at 1 15 19 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/9908c2af-8215-4a70-94fc-d8171902e6bb">

Inability to retrieve correct/enough passages:  
<img width="588" alt="Screenshot 2023-05-15 at 3 18 07 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/4e779bce-87da-44ac-b468-49f10c425fbc">

Limited/static number of retrieved documents:  
<img width="1069" alt="Screenshot 2023-05-15 at 3 20 51 PM" src="https://github.com/mbiss10/RAGdoll/assets/50077908/413b8ba1-cdf7-4782-a22d-d1ac23fac656">






