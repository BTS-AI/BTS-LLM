# -*- coding: utf-8 -*-

import requests
import json


class SkillSetFinalAnswerExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, skill_set_cot_request):
        headers = {
            "X-NCP-CLOVASTUDIO-API-KEY": self._api_key,
            "X-NCP-APIGW-API-KEY": self._api_key_primary_val,
            "X-NCP-CLOVASTUDIO-REQUEST-ID": self._request_id,
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "text/event-stream",
        }

        with requests.post(
            self._host + "/testapp/v1/skillsets/hay8ah4t/versions/4/final-answer",
            headers=headers,
            json=skill_set_cot_request,
            stream=True,
        ) as r:
            for line in r.iter_lines():
                if line:
                    print(line.decode("utf-8"))


if __name__ == "__main__":
    final_answer_executor = SkillSetFinalAnswerExecutor(
        host="https://clovastudio.stream.ntruss.com",
        api_key="NTA0MjU2MWZlZTcxNDJiY6GZWEz1p+pyDjIYUxazwBF3f1MDngJAYZ1nTSxVJrGV",
        api_key_primary_val="TBrJyPjFbqWK6rKZAOItq1LLybC5HBGYUjupDMZg",
        request_id="160bbf65-f942-45b2-b101-9b91b65c4818",
    )

    request_data = json.loads(
        """{
  "query" : "30대 남자 반팔 추천해줘",
  "tokenStream" : "False",
  "requestOverride" : {
	  "baseOperation": {
		"header": {
		  "X-Naver-Client-Id": "1IFgPA7ceaTdcSLRW8_M",
		  "X-Naver-Client-Secret": "qG1uE8l1HW"
		},
		"query": null,
		"requestBody": null
	  }
	}
	}""",
        strict=False,
    )

    final_answer_executor.execute(request_data)
    print(request_data)
