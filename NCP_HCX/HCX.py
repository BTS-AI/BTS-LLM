# -*- coding: utf-8 -*-
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            # 'Accept': 'text/event-stream'
        }

        try:
            with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                               headers=headers, json=completion_request, stream=True) as r:
                r.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킴
                full_response = ''
                for line in r.iter_lines():
                    if line:
                        decoded_line = line.decode("utf-8")
                        full_response += decoded_line
                return full_response
        except requests.exceptions.RequestException as e:
            print(f"HTTP 요청 실패: {e}")
            return None


def HCX_output_to_response(system, user):
    completion_executor = CompletionExecutor(
        host=os.getenv("CLOVA_X_HOST"),
        api_key=os.getenv("CLOVA_X_APIKEY"),
        api_key_primary_val=os.getenv("CLOVA_X_APIKEY_PRIMARY_VAL"),
        request_id=os.getenv("CLOVA_X_REQUEST_ID")
    )
    system = "너는 답변이 들어오는것을 그대로 출력해주는 역할을 합니다."+ system 
    preset_text = [{"role": "system", "content": system}, {"role": "user", "content": user}]

    request_data = {
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }

    response = completion_executor.execute(request_data)


    response_dict = json.loads(response)
    assistant_message = response_dict['result']['message']['content']
    return assistant_message


# print(HCX_output_to_response("도우미", "안녕하세요"))