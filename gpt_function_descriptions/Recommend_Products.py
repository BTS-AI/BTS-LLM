User_Recommend = [
    {
        "type": "function",
        "function": {
            "name": "Users_Recommend_Response",
            "description": """사용자가 원하는 상품을 추천 해달라고 질문했을 때, 사용자의 질문에 맞게 동작합니다. 
            

            # 예: 요즘 유행하는 5만원대 반팔티 추천해줘 => 함수를 호출합니다. => 호출된 함수에 데이터 값을 그대로 전달합니다
            # 예: 나에게 어울리는 가방 추천해줘 => 함수를 호출합니다. => 호출된 함수에 데이터 값을 그대로 전달합니다
            # 예: 바지 추천해줘 => 함수를 호출합니다. => 호출된 함수에 데이터 값을 그대로 전달합니다

            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": """ 사용자 질문을 그대로 전달합니다. """,
                    },
                    "category": {
                        "type": "string",
                        "description": "카테고리 이름, 예를 들면: '반팔', '치마', '바지'. '셔츠', '카라티셔츠, '민소매 티셔츠'",
                    },

                    "price_range": {
                        "type": "string",
                        "description": "사용자의 질문에서 가격대를 호출합니다. 예를 들면: '5만원이하', '5~10만원', '10~20만원'. '20~30만원', '30만원 이상',"
                    },
                },
                "required": ["text", "category", "price_range"],
            },
        },
    },

]
