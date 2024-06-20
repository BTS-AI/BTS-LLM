from datetime import datetime
from users.users_data import users_sample_data


# 현재 연도를 기준으로 나이를 계산하는 함수
def calculate_age(birth_date):
    birth_year = int(birth_date[:4])
    current_year = datetime.now().year
    return current_year - birth_year

# UserInfo 클래스 정의
class UserInfo:
    def __init__(self, data):
        self.data = data
        self.current_member = None

    def set_member_by_id(self, member_id):
        # 주어진 member_id에 해당하는 member를 찾기
        for member_data in self.data['data']:
            if member_data['member']['id'] == member_id:
                self.current_member = member_data['member']
                return True
        return False

    def get_info(self):
        if self.current_member:
            gender = '남자' if self.current_member['gender'] == 'M' else '여자'
            age = calculate_age(self.current_member['birth'])
            return {
                "name": self.current_member['name'],
                "nickName": self.current_member['nickName'],
                "profileImageUrl": self.current_member['profileImageUrl'],
                "gender": gender,
                "age": age,
                "height": self.current_member['height'],
                "footSize": self.current_member['footSize'],
                "MBTI": self.current_member['MBTI']
            }
        return None
    



user_info = UserInfo(users_sample_data[0])

# 특정 member_id로 설정

