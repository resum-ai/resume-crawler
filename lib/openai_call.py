import json

from openai import OpenAI

with open("secrets.json", "r") as file:
   secrets = json.load(file)

client = OpenAI(api_key=secrets["OPENAI_API_KEY"])

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   response = client.embeddings.create(input=[text], model=model).data
   response = response[0].embedding
   return response