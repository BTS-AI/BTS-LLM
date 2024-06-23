import os
import sys

from apis.weather import proc_weather
from NCP_HCX.load_retriever import output_to_response


from gpt_function_descriptions.weather_function_description import weather_function
from gpt_function_descriptions.Recommend_Products import User_Recommend


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# 모든 함수 목록
all_functions = weather_function + User_Recommend


# 사용 가능한 함수 목록을 업데이트하기 위한 함수
# 이 함수는 함수 이름들을 그들의 해당 실행 가능한 api들과 매핑
def update_available_functions():
    functions = all_functions
    available_functions = {}
    for function in functions:
        function_name = function["function"]["name"]

        if function_name.startswith("weather_"):
            available_functions[function_name] = proc_weather

        elif function_name.startswith("user_"):
            available_functions[function_name] = output_to_response

    return available_functions
