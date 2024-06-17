from dotenv import load_dotenv
from tool_function import tools
from HCX import HCX_output_to_response

from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent, create_openai_functions_agent

load_dotenv()

model = ChatOpenAI(model="gpt-4o")


SYSTEM_TEMPLATE = """



"""



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_TEMPLATE),
        MessagesPlaceholder("chat_history"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)



agent = create_openai_tools_agent(llm=model, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

message_history = ChatMessageHistory()

agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    # 대부분의 실제 시나리오에서 세션 ID가 필요하기 때문에 이것이 필요합니다
    # 여기서는 간단한 메모리 내 ChatMessageHistory를 사용하기 때문에 실제로 사용되지 않습니다
    lambda session_id: message_history,
    # 프롬프트의 질문이 입력되는 key: "input"
    input_messages_key="input",
    # 프롬프트의 메시지가 입력되는 key: "chat_history"
    history_messages_key="chat_history",
)


def output_to_response(input):
    response = agent_with_chat_history.invoke(
        {
            "input": input
        },
        # 세션 ID를 설정합니다.
        # 여기서는 간단한 메모리 내 ChatMessageHistory를 사용하기 때문에 실제로 사용되지 않습니다
        config={"configurable": {"session_id": "MyTestSessionID"}},
    )
    final_response = HCX_output_to_response(user=response['output'])
    print(f"답변: {final_response}")
    return final_response





try:
    while True:
        print("궁금한 것을 물어보세요")
        user_quote = input("엔터를 눌러 입력하거나 끝내시려면 ctrl + c를 입력하세요: ")
        result = output_to_response(user_quote)
except KeyboardInterrupt:
    print("종료중...")
