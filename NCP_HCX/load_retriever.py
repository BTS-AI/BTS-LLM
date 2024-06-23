import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from users.users_info import user_info


# 환경 변수 로드
load_dotenv()
model_name = "text-embedding-3-large"
embeddings = OpenAIEmbeddings(model=model_name)

load_path = "../../HCX_project/NCP_HCX/vectordb"

new_vectorstore = FAISS.load_local(
    load_path, embeddings, allow_dangerous_deserialization=True
)


member_id = 10001


def output_to_response(query):
    user_info.set_member_by_id(member_id)
    member_data = user_info.get_info()

    querys = f"{member_data['gender']}, {member_data['age']}" + query
    print(querys)
    vector_db_results = new_vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 5}
    ).invoke(querys)

    documents_content = ""
    for i, d in enumerate(vector_db_results):
        document_entry = f"\n## Document {i}.\n {d.page_content}\n\n"
        documents_content += document_entry

    return documents_content


# print((output_to_response("요즘 유행하는 반팔 추천해줘")))


# # output = new_vectorstore.get_relevant_documents(query)
# # print(results)
# # results = new_vectorstore.as_retriever().invoke("남자,20~24,상의,반팔, 요즘 유행하는 반팔 추천해줘")
# # print("0번", results[0].page_content)
# # print("1번", results[1].page_content)
# # print("2번", results[2].page_content)
# # print("3번", results[3].page_content)
# # print("4번", results[4].page_content)
