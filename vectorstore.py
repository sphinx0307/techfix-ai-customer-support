import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


class VectorStoreManager:

    def __init__(self):
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def build(self):

        documents = []

        kb_path = "knowledge_base"

        for file in os.listdir(kb_path):

            if file.endswith(".txt"):

                loader = TextLoader(
                    os.path.join(kb_path, file),
                    encoding="utf-8"
                )

                documents.extend(loader.load())

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documents)

        vector_db = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        return vector_db