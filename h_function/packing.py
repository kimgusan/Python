# # unpacking: 값을 풀어서 적는 것
# # def get_total(number1, number2, number3):
# #     return number1 + number2 + number3
#
#
# # packing: 값을 묶어서 적는 것
# def get_total(*numbers):
#     # 외부에서 전달받은 값들이 numbers(튜플)에 저장된다
#     print(numbers, type(numbers))
#     total = 0
#     for number in numbers:
#         total += number
#
#     return total
#
# # 여러 개의 값을 콤마로 구분하여 전달한다
# # total = get_total(1, 2, 3, 4, 5)
# # print(total)
#
#
# # 여러 개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통채로 들어가게 된다.
# # ([1, 2, 3, 4, 5], )
# # 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
#
# numbers = [1, 2, 3, 4, 5]
# total = get_total(*numbers)
# print(total)
#
# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# packing으로 제작하기
def get_total(name, *scores):
    print(name + '님')
    total = 0
    for score in scores:
        total += score
    return total

# print(get_total('김규산', 100, 40, 50))
#
# scores = [100, 40, 50]
# print(get_total('김규산', *scores))



# 문자열에서 'A' 가 몇 개 있는 지 검사하는 함수
# packing으로 제작하기

# def get_string(*string):
#     count = 0
#     for i in range(len(string)):
#         if 'A' in string[i]:
#             for j in string[i]:
#                 if j == 'A':
#                     count += 1
#     return count
#
#
# print(get_string('AAAasdAA', 'BBA'))

def get_count_of_A(*strs):
    # return [str.count('A') for str in strs]
    count = 0
    counts = []
    for str in strs:
        for s in str:
            if s == "A":
                count += 1
        counts.append(count)
        count = 0
    return counts

print(get_count_of_A("ABC", 'AAB', "AAA"))