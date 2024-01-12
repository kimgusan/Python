# f(x) = 2x + 1
# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)

# 두 정수의 곱셈 함수
def get_multi(number1, number2):
    return number1 * number2

# 두 정수의 나눗셈 후 몫과 나머지를 구하는 함수
def get_div(number1, number2):
    if number2 != 0:
        return number1 // number2, number1 % number2
    return None

# 1~10 까지 print()로 출력하는 함수
def print_ten():
    for i in range(10):
        print(i+1, end = ' ')

# 이름을 n번 print()로 출력하는 함수
def call_name(name, n):
    for i in range(n):
        print(name)
    # print(name * n)

# 1~n 까지의 합을 구해주는 함수
def get_sum(n):
    total = 0
    for i in range(n):
        total += (i+1)
    return total

# 1~100까지 중 n의 배수를 print()로 출력하는 함수
def get_drainage(n):
    for i in range(100):
        if (i+1) % n == 0:
            print(i+1, end=' ')

# 세 정수의 뺄셈 함수
def get_minus(number1, number2, number3):
    return number1 - number2 - number3


# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
# def call_count(string, str):
#     count = 0
#     for i in string:
#         if i == str:
#             count += 1
#     return count

def get_count_of_result(target, keyword):
    return len([i for i in target if i == keyword])


'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''
def find(string, str):
    for i in range(len(string)):
        if string[i] == str:
            return i
    return -1




