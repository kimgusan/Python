# student = {
#     "name" : "김규산",
#     "email": "kimgusan@naver.com"
# }
#
# print(student['name'])
# print(student.get('name'))
#
# # get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이가능하며,
# # default 값이 없을 때에는 None을 가져온다
# #print(student['phone']) # 오류
# print(student.get('phone', '0101231234'))
#
# # 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다
# student['name'] = '신짱구'
# print(student)
#
# # 'phone' key 값이 없기 때문에 아래의 코드는 '추가'이다.
# student['phone'] = '0101231234'
# print(student)
#
#
# if 'email' in student: # 수정
#     student['email'] = 'hgd@gmail.com'
# else: #추가
#     student['email'] = 'hgd@gmail.com'
#
# print(student)

my_dict = {
    1: '김규산',
    'two': "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age": 40},
        {"name": "jack", "age": 30},
        {"name": "john", "age": 20},
    ]
}

# row에 있는 회원 3명의 정보를 모두 출력

# if 'row' in my_dict:
#     for data in range(len(my_dict['row'])):
#         result = my_dict['row'][data]['name']
#         print(result, end = ' ')

if 'row' in my_dict:
    for data in my_dict['row']:
        print(f'{data["name"]}, {data["age"]}')



# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.


#1

# number_dict = {
#     True: [i * 2 + 1 for i in range(5)],
#     False: [(i + 1) * 2 for i in range(5)]
# }

# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ')])))
# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ') == '홀수'])))

# dic1 = {"홀수": [1, 3, 5, 7, 9], "짝수": [2, 4, 6, 8, 10]}
# if user_input == '홀수':
#     print(dic1[user_input])
# else:
#     print(dic1[user_input])

student = {
    "name" : "김규산",
    "email": "kimgusan@naver.com"
}

# key분리
print(list(student.keys()))

# value 분리
print(list(student.values()))

# item 분리
print(list(student.items()))

for key, values in student.items():
    print(key, values)

print(1500*1.5)
print(1500*0.5)

print(round(123.444,2))