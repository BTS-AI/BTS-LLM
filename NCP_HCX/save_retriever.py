from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


# 환경 변수 로드
load_dotenv()

loaders = [
    CSVLoader("/Users/sbk/code/NCP_HCX/data/sample_data.csv"),
]

# 문서 로드 및 분할
docs = []
for loader in loaders:
    docs.extend(loader.load())

model_name = "text-embedding-3-large"
embeddings = OpenAIEmbeddings(model=model_name)

vectorstore = FAISS.from_documents(docs, embeddings, distance_strategy="cosine")

# retriever = vectorstore.as_retriever()

save_path = "/Users/sbk/code/NCP_HCX/vectordb"
vectorstore.save_local(save_path)
