from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


# 환경 변수 로드
load_dotenv()

loaders = [
    CSVLoader("/Volumes/Extreme SSD/code_products/products/befor_code/code/HCX_project/NCP_HCX/data/데이터완성.csv"),
]

# 문서 로드 및 분할
docs = []
for loader in loaders:
    docs.extend(loader.load())

model_name = "text-embedding-3-large"
embeddings = OpenAIEmbeddings(model=model_name)

# vectorstore = FAISS.from_documents(docs, embeddings, distance_strategy="cosine")

index_name = "hcx-data"

vectorstore = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
# retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 1})
# print("반팔추천해줘")

# retriever = vectorstore.as_retriever()

# save_path = "/Volumes/Extreme SSD/code_products/products/befor_code/code/HCX_project/NCP_HCX/vectordb"
# vectorstore.save_local(save_path)
