import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dotenv import load_dotenv
# from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from users.sample_users_data import get_user_by_id
from langchain_pinecone import PineconeVectorStore


# 환경 변수 로드
load_dotenv()
model_name = "text-embedding-3-large"
embeddings = OpenAIEmbeddings(model=model_name)


index_name = "hcx-data"

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)


member_id = "tomy"


def Users_Recommend_Response(query, category, price_range):
    member_data = get_user_by_id(member_id)

    # querys = f"'성별:'{ member_data['gender']}, '카테고리1: 반소매티셔츠', '나이:'{member_data['age']}, '가격대: 5만원 이하', '질문:'", + query
    querys = f"성별: {member_data['sex']}, 카테고리: {category}, 연령대: {member_data['age']}, 가격대: {price_range}, 질문: {query} 추천해줘"
    print(querys)
    vector_db_results = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ).invoke(querys)

    documents_content = ""
    for i, d in enumerate(vector_db_results):
        document_entry = f"\n## Document {i+1}.\n {d.page_content}\n\n"
        documents_content += document_entry

    return documents_content


# print((Users_Recommend_Response("요즘 유행하는 반팔 추천해줘")))


# results = vectorstore.as_retriever().invoke("남자,20~24,상의,반팔, 요즘 유행하는 반팔 추천해줘")
# print("0번", results[0].page_content)
# print("1번", results[1].page_content)
# print("2번", results[2].page_content)
# print("3번", results[3].page_content)
# print("4번", results[4].page_content)
