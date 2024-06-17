from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings 

# 환경 변수 로드
load_dotenv()
model_name = "text-embedding-3-large"
embeddings = OpenAIEmbeddings(model=model_name)

load_path = "/Users/sbk/code/NCP_HCX/vectordb"

new_vectorstore = FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
query = "남자,20~24,상의,반팔, 요즘 유행하는 반팔 추천해줘"
results = new_vectorstore.similarity_search(query)
# output = new_vectorstore.get_relevant_documents(query)
# print(results)
# results = new_vectorstore.as_retriever().invoke(query)
# print("0번", results[0].page_content)
# print("1번", results[1].page_content)
# print("2번", results[2].page_content)
# print("3번", results[3].page_content)
# print("4번", results[4].page_content)