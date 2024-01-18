from crud_module import *

if __name__ == '__main__':
    # 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
    # 아이디(이메일) 중복검사
    message = '아이디: '
    member_id = input(message)
    find_by_id_query = "select email from tbl_member where email = %s"
    find_by_id_params = member_id,
    result = find_by_id(find_by_id_query,find_by_id_params)
    if result:
        message = "비밀번호"
        password = input(message)




# 로그인 후 마이페이지로 이동
email = input('이메일을 입력해주세요')
password = input('비밀번호를 입력해주세요')

find_by_id_query = "select email, password, name from tbl_member where email = %s"
params = [email]
user = find_by_id(find_by_id_query, params)
if user is not None:
    if password == user.get('password'):
        print(user)
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('이메일이 없습니다.')


# 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사  /// o_api.standard.mail_module /// random_module

# 사용자가 입력한 한국어를 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 전체 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
# 경로와 추출한 텍스트 전체 조회








----