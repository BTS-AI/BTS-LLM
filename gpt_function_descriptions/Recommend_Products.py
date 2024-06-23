User_Recommend = [
    {
        "type": "function",
        "function": {
            "name": "user_recommend",
            "description": """사용자가 추천 해달라고 질문했을 때, 사용자의 질문에 맞게 동작합니다. 
            상품 카테고리 정보가 들어오지 않을경우 '상품 카테고리를 알려주세요' 라는 메시지를 호출합니다.

            # 예: 요즘 유행하는 반팔티 추천해줘 => 함수를 호출합니다.
            # 예: 요즘 유행하는 치마 추천해줘 => 함수를 호출합니다.
            # 예: 요즘 유행하는 바지 추천해줘 => 함수를 호출합니다.


                   
            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": """ 사용자 질문에서 추천하고자 하는 상품을 추출합니다. """,
                    },
                    "category": {
                        "type": "string",
                        "description": "카테고리 이름, 예를 들면: '반팔', '치마', '바지'. '셔츠', '카라티셔츠, '민소매 티셔츠'",
                    },
                },
                "required": ["text"],
            },
        },
    },
]
