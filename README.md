# pendRAGon

A RAG model for conversational course reccomendations.

<img width="1002" alt="Screenshot 2023-04-25 at 2 19 23 PM" src="https://user-images.githubusercontent.com/50077908/234376165-81912dfa-e2aa-43fb-9b58-a353a2d25117.png">

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
