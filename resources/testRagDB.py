"""
Извлича информация по текст от векторна база(семантично търсене)
"""
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import json
from pathlib import Path
from pprint import pprint

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
# query = "Каква е презумпцията за невинност според гражданското право?"
query = "Каква е глобата за каране с превишена скорост 20 км над ограничението на скоростта?"

db = Chroma(persist_directory="C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\chroma_db", embedding_function=embeddings)
docs = db.similarity_search(query)
print(docs[0].page_content)