# pendRAGon

A RAG model for conversational course reccomendations.

<img width="1002" alt="Screenshot 2023-04-25 at 2 19 23 PM" src="https://user-images.githubusercontent.com/50077908/234376165-81912dfa-e2aa-43fb-9b58-a353a2d25117.png">

### Repository Overview:
- `data` stores our input copora, questions, and reference answers to evaluate our model. The dev set is based on the CSCI department and the test set is based on the MATH department. 
- `evaluation` stores all the files used to evaluate our model. It contains a `human_scores` directory, which contains human evaluation of the model's correctness. Additionally, it contains an `output` repo, which contains auto-generated files containing the results of our evaluation using the ROUGE and BLEU metrics. Finally, it conatains `evaluate.py`, a script responsible for generating the files in output.
- `results` stores the results of each model run. It contains both a plain text and pickled representation of the model's history (i.e. the questions it was asked, its responses to said questions, and the sources it consulted to answer each question.


### Messy Stuff:
Using `Python 3.8.16`

System Requirements (install using Homebrew):
- `poppler`
- `tesseract`

Library Requirements:
- `langchain`
- `openai`
- `dotenv`
- `tiktoken`
- `faiss-cpu`
- `unstructured` 
  - (install using `pip install "unstructured[local-inference]"`)
- `detectron2`
  - (install using `pip install 'git+https://github.com/facebookresearch/detectron2.git@e2ce8dc#egg=detectron2'`)


More info [here](https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/unstructured_file.html)
