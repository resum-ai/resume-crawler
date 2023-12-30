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

with open("secrets.json", "r") as file:
   secrets = json.load(file)

pinecone.init(api_key=secrets["PINECONE_API_KEY"], environment="gcp-starter")


if __name__ == '__main__':
    print("Hello VectorStore!")

    conn = sqlite3.connect('crawling_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


    # loader = TextLoader('/Users/jang-youngjoon/dev-projects/intro-to-vector-db/mediumblogs/mediumblog1.txt')
    # document = loader.load()
    #
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # texts = text_splitter.split_documents(document)
    # print(len(texts))
    #
    # embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    #
    # docsearch = Pinecone.from_documents(texts, embeddings, index_name="medium-blogs-embeddings-index")
    #
    # qa = RetrievalQA.from_chain_type(
    #     llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(), return_source_document=True
    # )
    # query = "What is a vector DB? Give me a 15 word answer for a beginner"
    # result = qa({"query": query})
    # print(result)
