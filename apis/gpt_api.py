import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

# .env로 API KEY 가져오기
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
gpt_4model = "gpt-4-1106-preview" #gpt-4-1106-preview, gpt-3.5-turbo-0613
gpt_3model = "gpt-3.5-turbo-0125"


# 최신 gpt를 사용하기 위한 formet
def gpt_response(msg):
    response = client.chat.completions.create(
        model=gpt_4model,
        messages=[{"role":"user", "content":msg}],
        max_tokens=500,
        temperature=0.5
    )

    # response = response.to_dict_recursive()
    response = response.choices[0].message.content
    return response