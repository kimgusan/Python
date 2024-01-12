# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
# # 추가
# def insert(*, number, name):
#     '''
#     :param number: 회원 번호
#     :param name: 회원 이름
#     '''
#     user_info.append({'number': number, 'name': name})
#
# # insert(number=6, name='hong')
# # print(user_info)
#
# # 목록
# def list():
#
#     user_name = [user_info[i]['name'] for i in range(len(user_info))]
#     numbers = [user_info[i]['number'] for i in range(len(user_info))]
#
#     return f"user_name: {user_name}\nnumbers: {numbers}"
# # print(list())
#
# # 조회(번호로 조회)
# def find(*, number):
#     '''
#     :param number: number= 찾는 번호
#     :return: 이름값
#     '''
#     user_name = [user_info[i]['name'] for i in range(len(user_info))]
#     numbers = [user_info[i]['number'] for i in range(len(user_info))]
#
#     if number in numbers:
#         return user_name[numbers.index(number)]
#     else:
#         return None
#
# # print(find(number = 2))
#
# # 수정(번호로 이름 수정)
# def update(choice_number):
#     '''
#
#     :param choice_number:  1: number 수정 , 2: name 수정
#     '''
#     user_name = [user_info[i]['name'] for i in range(len(user_info))]
#     numbers = [user_info[i]['number'] for i in range(len(user_info))]
#
#     if choice_number == 'number':
#         number = int(input("수정전 변경하고 싶은 번호 입력:"))
#         if number in numbers:
#             re_number = int(input("수정 후 변경되어야 할 번호 입력:"))
#             user_info[numbers.index(number)]['number'] = re_number
#             return print("숫자가 수정 되었습니다")
#         else:
#             return print("없는 숫자 입니다.")
#
#     elif choice_number == 'name':
#         re_name = input("수정전 변경하고 싶은 이름 입력:")
#         if re_name in user_name:
#             update_name = input("수정 후 변경 되어야할 이름 입력:")
#             user_info[user_name.index(re_name)]['name'] = update_name
#             return print("이름이 수정 되었습니다")
#         else:
#             return print("이름이 없습니다.")
#     else:
#         None
#
# # update('number')
#
# # 삭제(번호로 조회)
#
# def delete(*, number):
#     numbers = [user_info[i]['number'] for i in range(len(user_info))]
#
#     if number in numbers:
#         del user_info[number-1]
#         print(user_info)
#     else:
#         None
#
#
# # delete(number = 5)
# ### =================================================================================================
# # 강사님코드
#
# # 추가
# def insert(*, number, name):
#     '''
#     :param number: 회원 번호
#     :param name: 회원 이름
#     '''
#     user_info.append({'number': number, 'name': name})
#
# # 추가
# # 회원 번호는 자동 증가한다
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
# # 목록
# def select_all():
#     return user_info
# print(select_all())
#
# # 조희(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#     :param kwargs: 'number': 기존 회원번호, 'name' : 새로운 회원 이름
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
# update(number=1, name= 'han')
# print(select_all())
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#
# delete(1)
# print(select_all())
# insert(name='hong')
# print(select_all())
#
# ### ===============================================================================================================
# 실습
# post_info = [
#     {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
#     {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
#     {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
#     {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
#     {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
# ]
#
# # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# read_count = 0
# number = 5
# def post_append(**kwargs):
#     '''
#     :param kwargs: number: 유니크한 숫자, title: 테스트제목 + number, content: 테스트내용+number, file: 주소값+number, read_count: 조회수(default = 0)
#     '''
#
#     global number
#     number += 1
#     post_info.append({'number': number, 'title': kwargs.get('title')+ str(number), 'content': kwargs.get('content')+ str(number), 'file': kwargs.get('file'), 'read_count': 0})
#     return f"추가 완료"
#
# # print(post_append( title= '테스트 제목', content='테스트 내용', file='/usr/post/file/img00.png'))
#
# # 목록(최신순으로 조회)
# def select_all():
#
#     result = []
#     max = len(post_info)
#     for i in range(max):
#         result.append(post_info[i])
#     return result
#
# # print(select_all())
# # select_all()
#
# # 조회(번호로 조회, 조회수 1 증가)
# def select_one(number):
#
#     for i in range(len(post_info)):
#         if post_info[i]['number'] == number:
#             post_info[i]['read_count'] += 1
#             return post_info[i]
# print(select_one(1))
#
# # 수정(번호로 정보 수정)
# def update(*, number, **kwargs):
#
#     for i in range(len(post_info)):
#         if post_info[i]['number'] == number:
#             post_info[i]['title'] = kwargs.get('title')
#             post_info[i]['content'] = kwargs.get('content')
#             post_info[i]['file'] = kwargs.get('file')
#         else:
#             None
#     print(post_info)
#
#
# # update(number= 1, title='hello', content = 3000)
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     for i in range(len(post_info)):
#         if post_info[i]['number'] == number:
#             del post_info[i]
#         return post_info
#
# print(delete(1))
# =================================================================================

# 실습
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)

number = 5


def insert(**kwargs):
    global number
    number += 1
    post = {
        'number': number,
        'title': kwargs.get('title'),
        'content': kwargs.get('content'),
        'file': kwargs.get('file'),
        'read_count': 0}
    post_info.append(post)


# 목록(최신순으로 조회)
def select_all():
    return post_info[::-1]


# 조회(번호로 조회, 조회수 1 증가)
def select(number):
    for post in post_info:
        if post['number'] == number:
            return post


def read(number):
    post = select(number)
    post['read_count'] += 1
    return post


# 수정(번호로 정보 수정)
def update(**kwargs):
    post = select(kwargs['number'])
    print(post)


update(number=1)

# 삭제(번호로 삭제)
