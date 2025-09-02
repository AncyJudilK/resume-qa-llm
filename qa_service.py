import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI

documents = SimpleDirectoryReader("data/resume.txt").load_data()

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

llm = OpenAI(model="gpt-3.5-turbo")

query_engine = index.as_query_engine(llm=llm)
