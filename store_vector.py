import os
import sqlite3

from langchain.document_loaders import TextLoader
from langchain.llms.openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain.chains import RetrievalQA
import json

from lib.openai_call import get_embedding
from lib.store import chunks, generate_data

with open("secrets.json", "r") as file:
   secrets = json.load(file)

pinecone.init(api_key=secrets["PINECONE_API_KEY"], environment="gcp-starter")

index = pinecone.Index('resumai-self-introduction-index')

#데이터 로딩
conn = sqlite3.connect('crawling_data.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM data")
datas = cursor.fetchall()

conn.close()

with pinecone.Index('resumai-self-introduction-index', pool_threads=30) as pinecone_index:
    async_results = [
        pinecone_index.upsert(vectors=ids_vectors_chunk, async_req=True)
        for ids_vectors_chunk in chunks(generate_data(datas), batch_size=100)
    ]
    [async_result.get() for async_result in async_results]


