# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30
print(a, b, c, sep = ', ')

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

# temp = a
# a = b
# b = temp
# print(a, b)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))

a = 10.5
print(type(a))

a = 'A'
print(type(a))

a = "ABC"
print(type(a))

a = ['A', 'B', 'C']
print(type(a))

a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))

a = True
print(a, type(a))

#변수명 주의사항
int_type = 10
print(type(int_type))

float_type = 10.5
print(type(float_type))

str_type = 'A'
print(type(str_type))

string_type = "ABC"
print(type(string_type))

list_type = ['A', 'B', 'C']
print(type(list_type))

dict_type = {'A': 1, 'B': 2, 'C': 3}
print(type(dict_type))

bool_type = True
print(bool_type, type(bool_type))

# 서식문자
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로, 32.75로 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even)이라고 한다.
name = '김규산'
age = 20
height = 157.55

# print("이름: %s" % name)
# print("나이: %d" % age)
# print("키: %.1f" % height)
print("이름: %s\n나이: %d살\n키: %.1fcm" % (name, age, height))

print("=" * 20)
formatting = "이름: %s\n나이: %d살\n키: %.1fcm" % (name, age, height)
print(formatting)
print("=" * 20)

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기 (서식문자 사용 %)
# 1 + 3 = 4

print("=" * 40)
num1 = 1
num2 = 3
total = num1 + num2
print("%d + %d = %d" % (num1, num2, total))

print("=" * 40)

# format 함수
name = "홍길동"
age = 80
height = 156.26
print("이름: {}\n나이: {}\n키: {:.1f}" .format(name, age, height))
print("이름: {0}\n나이: {1}\n키: {2:.1f}" .format(name, age, height))
print("이름: {name}\n나이: {age}\n키: {height:.1f}" .format(name=name, age=age, height=height))

formatting1 = "이름: {}\n나이: {}\n키: {:.1f}" .format(name, age, height)
formatting2 = "이름: {0}\n나이: {1}\n키: {2:.1f}" .format(name, age, height)
formatting3 = "이름: {name}\n나이: {age}\n키: {height:.1f}" .format(name=name, age=age, height=height)

print(formatting1)
print(formatting2)
print(formatting3)

# 실습
# 아래 메세지를 format함수를 사용하여 출력한다
# Hello 파이썬, Python is fantasic !
# Hello 장고, Django is fantasic !
# Hello 리액트, React is fantasic !

print("=" * 40)
language1 = "파이썬"
e_language1 = 'Python'

language2 = "장고"
e_language2 = 'Django'

language3 = "리액트"
e_language3 = 'React'

# 자동으로 해당 순서에 값이 반영된다
result1 = "Hello {}, {} is fantastic !" .format(language1, e_language1)

# 값에 할당된 번호를 작성하면 해당 값이 반영된다.
result2 = "Hello {0}, {1} is fantastic !" .format(language2, e_language2)

# 값에 이름을 붙이면 해당 이름에 있는 값이 반영된다
result3 = "Hello {kor}, {eng} is fantastic !" .format(kor=language3,eng=e_language3)

print(result1)
print(result2)
print(result3)
print(result1, result2, result3, sep='\n')
print("=" * 40)

# format string
name = '한동석'
age = 20
height = 156.26

#round(실수값, 반올림 자리수)
print(f"이름: {name}")
print(f"나이: {age}")
print(f"키: {round(height, 1)}")

# 실습
# 아래 메세지를 f-string함수를 사용하여 출력한다
# Hello 파이썬, Python is fantasic !
# Hello 장고, Django is fantasic !
# Hello 리액트, React is fantasic !

print("=" * 40)
print(f"Hello {language1}, {e_language1} is fantasic !")
print(f"Hello {language2}, {e_language2} is fantasic !")
print(f"Hello {language3}, {e_language3} is fantasic !")

result1 = f"Hello {language1}, {e_language1} is fantastic !"
result2 = f"Hello {language2}, {e_language2} is fantastic !"
result3 = f"Hello {language3}, {e_language3} is fantastic !"
print(result1, result2, result3, sep='\n')
print("=" * 40)