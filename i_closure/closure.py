def set_key(key):
    formatting = ''

    # 클로저
    def set_value(value):
        nonlocal formatting
        formatting = f"{key}: {value}"
        return formatting

    return set_value

# set_name = set_key('이름')
# formatting_name = set_name('한동석')
# print(formatting_name)

# '나이: 00살'
def get_title(title):
    age = ''

    def get_age(ages):
        nonlocal age
        age = f"{title}: {ages}살"
        return age

    return get_age

# set_age = get_title('나이')
# formatting = set_age(30)
# print(formatting)
# =====================================================

# # '나이: 00살'
# set_name = set_key('나이')
# formatting_age = set_name("20살")
# print(formatting_age)
# print(f'{formatting_name}\n{formatting_age}')

# 실습1
# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름" =>이런 형식 리턴
# 함수2. "전달받은 주제, 전달받은 요약" => 이런 형식 리턴
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

def set_topic(**kwargs):
    if 'name' in kwargs:
        re_name = kwargs['name']

        def set_funtion1(real_name):
            nonlocal re_name
            re_name = real_name
            kwargs['name'] = re_name
            return f"name, {kwargs['name']}"
    else:
        None

    return set_funtion1

# return_name = set_topic(name = '김규산')
# formatting = return_name('신짱구')
#print(formatting)

# 실습2
# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

def set_product(*args):
    number = 1
    arg = list(args)
    result = 0

    def set_format(name):
        nonlocal arg
        arg.append(name)
        args = tuple(arg)
        formatting = args
        return formatting

    def get_update(infomation):
        nonlocal arg
        if infomation in arg:
            u_fruit = input("수정하고 싶은 과일명:")
            index = arg.index(infomation)
            arg[index] = u_fruit
            args = tuple(arg)
            formatting = args
            return formatting
        else:
            return "수정할 과일이 없습니다"

    def select_all():
        formatting = args

        return formatting

    return select_all

get_product = set_product('사과', 1000, '배', 2000)
# print(get_product('자두'))
get_update = set_product('사과', 1000, '배', 2000)
# print(get_update('자두'))
# print(get_update('수박'))
print(get_update())

