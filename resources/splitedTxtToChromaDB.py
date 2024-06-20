"""
Създава векторна база от данни с помощта на text-embedding-3-large модела на OpenAI
"""
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from pathlib import Path
from pprint import pprint

loader = TextLoader("C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\output_document.txt", encoding='utf-8')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=8100, chunk_overlap=200, separator="</$>"
)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", show_progress_bar=True, chunk_size=3)
db2 = Chroma.from_documents(docs, embeddings, persist_directory="C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\chroma_db")