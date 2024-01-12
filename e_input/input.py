# 문자열끼리만 연결(+)이 가능하다
# data = 3
# print('안' + str(data))
# name = input("이름: ")
# formatting = f"{name}님 환영합니다."
# print(formatting)
# print(f"{name}님 환영합니다.")
#
# # 제 이름은???, 제 키는 ???cm 입니다.
# name = input("이름을 입력 하세요: ")
# height = input("키를 입력 하세요: ")
# result = f"제 이름은 {name}, 제 키는 {height}cm 입니다."
# print(result)

# 두 정수를 입력 받은 후 곱셈 결과 출력
# num1 = int(input("정수1: "))
# num2 = int(input("정수2: "))
# result = num1 * num2
# formatting = f"{num1} * {num2} = {result}"
# print(formatting)
#
# # 강사님 풀이
# # 1) map 함수 사용
# map(각각 어떻게 바꿀 것인가, [])
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# fomatting = f"{number1} * {number2} = {result}"
# print(fomatting)
#
# # 2) 변수 사용
# message1 = '첫 번째 정수: '
# message2 = '두 번째 정수: '
#
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
# formatting = f"{number1} * {number2} = {result}"
#
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message = '현재 시간을 입력하세요 '
example_message = '예) 00:00'
hour, minute = map(str, input(message + example_message +'\n').split(':'))
result = f'현재 시간은 {hour}시 {minute}분 입니다'
print(result)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
phone_number = '핸드폰 번호를 입력하세요'
example_message = '예) 010-xxxx-xxxx'
phone_number1, phone_number2, phone_number3 = map(str, input(phone_number + example_message + '\n').split('-'))
result = f"핸드폰 번호의 각 자리수는 {phone_number1}, {phone_number2}, {phone_number3}입니다"
print(result)

# 이름과 나이를 한 번에 입력 받은 뒤 "000"님의 나이는 000살" 형식으로 출력
message = '이름과 나이를 입력하세요: '
example_message = '예)김규산 30'
name, age = map(str, input(message + example_message + '\n').split())
result = f"{name}님의 나이는 {age}살"
print(result)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message = '3개의 정수를 입력하세요'
example_message = ' ex)1,2,3'
num1, num2, num3 = map(int, input(message + example_message + '\n').split(','))
sum = num1 + num2 + num3
result = f'{num1} + {num2} + {num3} = {sum}'
print(result)