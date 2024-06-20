import os
import sys
import time

# 상위 디렉토리에 있는 모듈을 가져오기 위해 경로를 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pprint import pprint
from utils.printer import ColorPrinter as Printer  
from utils.input_memory import User_Input_Memory  
from available_functions import update_available_functions  
from available_functions import all_functions  
from function_to_call import tool_call_function  
from apis.gpt_api import gpt_3model, gpt_4model  
from apis.gpt_api import client  
from NCP_HCX.HCX import HCX_output_to_response
from prompt_setups.system_setup import HCX_SYSTEM_SETUP
from utils.messages_parse import parse_messages



Input_memory = User_Input_Memory()

def ask_gpt_functioncall(query):
    # 사용자의 입력들을 가져오기
    Input_memory.add_question(query)
    last_questions = Input_memory.last_questions()
    append_user_input = '\n'.join(last_questions)
    system_user_input = HCX_SYSTEM_SETUP + append_user_input

    try:
        start_time = time.time()  # 시작 시간을 측정

        # 페르소나 입력
        messages = [{"role": "system", "content": system_user_input}]
        # 마지막 질문들을 메시지 목록에 추가
        # messages.extend([{"role": "user", "content": q} for q in last_questions])
        # 현재 질문을 메시지 목록에 추가
        messages.append({"role": "user", "content": query})

        # GPT의 tool 호출에 응답하기 위해 사용할 수 있는 함수 목록
        tools = all_functions

        # 사용자 쿼리와 시스템설정(페르소나)을 포함한 GPT에 초기 설정
        first_response = client.chat.completions.create(
            model=gpt_3model,
            messages=messages,
            temperature=0.0,
            tools=tools,
            tool_choice="auto",  # default: "auto"
        )

        # GPT의 첫 번째 응답에서 메시지만 파싱
        first_response_message = first_response.choices[0].message

        # 첫번째 GPT의 답변을 메시지의 추가 
        # tool_calls가 있으면 설정된 도구 및 api를 불러오고 아니면 GPT가 답변을 위한 메시지 어팬드 
        messages.append(first_response_message) 

        # 첫번째 메시지에서 tool_calls를 추출
        tool_calls = first_response_message.tool_calls
        # pprint(tool_calls)

            # tool_calls가 있으면, 쿼리를 기억하지 않습니다.
            # if not tool_calls:
            #     Input_memory.add_question(query)

            # GPT의 응답에 tool_calls가 포함되어 있으면, 이를 처리
        if tool_calls:
            # 사용 가능한 함수 목록 업데이트
            available_functions = update_available_functions()

            # 각 함수마다 매핑된 함수를 호출
            for tool_call in tool_calls:
                tool_call_response = tool_call_function(tool_call, available_functions)

                # tool_call가 성공적으로 처리되면, 그 응답을 대화 기록에 추가
                if tool_call_response:
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_call.function.name,
                        "content": tool_call_response,
                    })

            # tool_call 응답을 포함한 업데이트된 대화 기록으로 GPT에 후속 요청
            # print(messages)

            # print('HCX_MSG: ', type(HCX_MSG))
            HCX_system,  HCX_user = parse_messages(messages)
            # print(parse_messages(messages))
            second_response_message = HCX_output_to_response(HCX_system, HCX_user)  # 문자열 양쪽 공백 제거
            
            # print(second_response_message)
            # 사용자가 볼 수 있도록 전체 대화와 최신 응답을 출력
            Printer.color_print(messages)
            pprint(second_response_message)
            end_time = time.time()  # 종료 시간을 측정
            print(f"걸린시간: {end_time - start_time} 초")  # 실행 시간을 출력.
            return second_response_message

        # 첫 번째 응답에 tool_call이 없으면 출력
        pprint(first_response_message.content)
        end_time = time.time()
        print(f"걸린시간: {end_time - start_time} 초")
        return first_response_message.content



    except Exception as e:
        # 함수 호출 중 발생할 수 있는 예외를 처리하고 디버깅을 위한 오류 메시지를 제공.
        print(f"에러메시지: {e}")
        return None


try:
    while True:
        print("궁금한것을 물어보세요")
        user_quote = input("엔터를 눌러 입력하거나 끝내시려면 ctrl + c를 입력하세요: ")
        result = ask_gpt_functioncall(query=user_quote)
except KeyboardInterrupt:
    print("종료중...")
