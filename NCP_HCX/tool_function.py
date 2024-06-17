from load_retriever import new_vectorstore
from langchain.tools.retriever import create_retriever_tool


retriever = new_vectorstore.as_retriever(k=3)

men_2024_Short_shirt_tool = create_retriever_tool(
    retriever,
    "style_recommendation",
    "20대 남자의 반팔을 추천해주는 도구야",
)


tools = [men_2024_Short_shirt_tool]
