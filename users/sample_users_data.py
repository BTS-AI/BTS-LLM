import json

# JSON 형식의 데이터
data = '''
[
    {
        "age": 29,
        "birth": "1995.06.05",
        "id": "tomy",
        "name": "Tomy",
        "no": 3,
        "sex": "남자"
    },
    {
        "age": 29,
        "birth": "1995.06.20",
        "id": "ruby",
        "name": "루비",
        "no": 5,
        "sex": "여자"
    },
    {
        "age": 10,
        "birth": "2014.05.21",
        "id": "core",
        "name": "코어",
        "no": 7,
        "sex": "남자"
    },
    {
        "age": 28,
        "birth": "1996.06.10",
        "id": "jason",
        "name": "제이슨",
        "no": 8,
        "sex": "남자"
    }
]
'''

# JSON 데이터 파싱
parsed_data = json.loads(data)

def get_user_by_id(user_id):
    # user_id와 일치하는 사용자 정보를 찾아 반환
    for user in parsed_data:
        if user['id'] == user_id:
            return user
    return None  # 일치하는 사용자가 없을 경우 None 반환

# 사용 예시
# user_id = 'tomy'  # 찾고자 하는 사용자의 id
# user_info = get_user_by_id(user_id)


# 파싱된 데이터 출력
# for person in parsed_data:
#     print(f"Name: {person['name']}, Age: {person['age']}, Birth: {person['birth']}, ID: {person['id']}, No: {person['no']}, Sex: {person['sex']}")


# print(parsed_data)