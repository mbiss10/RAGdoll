# pendRAGon

A RAG model for conversational course reccomendations.


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