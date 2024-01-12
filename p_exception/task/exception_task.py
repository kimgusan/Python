# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여, 발생 시 안내 메세지까지 출력하기

class NickNameError(Exception):
    def __str__(self):
        return "비속어는 사용할 수 없습니다."

def check_nickname(nickname: str):
    bad_word = ['바보', "멍게", "해삼", "운영자"]

    for word in bad_word:
        if word in nickname:
            raise NickNameError


nickname = input('닉네임: ')
try:
    check_nickname(nickname)
    print(nickname)
except NickNameError as nick_error:
    print(nick_error)





