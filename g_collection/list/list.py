# # animals = ["dog", "cat", "bird", "fish"]
# #
# # print(id(animals))
# # print(type(animals))
# #
# # # 인덱스로 접근
# # print(animals[1])
# # print(animals[2])
# #
# # # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
# # print(animals[-1])
# # print(animals[-2])
# #
# # # len()
# # print(len(animals))
# #
# # # append()
# # animals.append("hamster")
# # print(len(animals))
# # print(animals)
# #
# # animals.append("cat")
# # print(animals)
# #
# # # insert()
# # animals.insert(1, "dog")
# # print(animals)
# #
# # # remove()
# # animals.remove("fish")
# # print(animals)
# #
# # # del()
# #
# # # del(animals[1])
# # del animals[1]
# # print(animals)
# #
# # #clear()
# # # animals.clear()
# # # print(animals)
# #
# # # index()
# # print(animals.index('bird'))
# # # print(animals.index('tiger')) #ValueError: 'tiger' is not in list
# #
# # # 수정
# # # animals[animals.index('bird')] = 'lion'
# # index = animals.index('bird')
# # animals[index] = 'lion'
# # print(animals)
# #
# # # 그 외
# # animals = ["dog", "cat", "bird", "fish"]
# # print(animals * 2)
# #
# # print('dog' in animals)
# # print('tiger' in animals)
# #
# # for animal in animals:
# #     print(animal)
#
# # 실습
# # 1~90까지 list 에 담고 출력
# li1 = list(range(1,91))
# print(li1)
#
# number_list = [0] * 90
# for i in range(len(number_list)):
#     number_list[i] = i + 1
# print(number_list, end = '\n')
#
# # 1~100까지 중 짝수만  list 에 담고 출력
# li2 = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         li2.append(i)
# print(li2)
#
# number_list = [0] * 50
# for i in range(len(number_list)):
#     number_list[i] = (i + 1) * 2
# print(number_list, end = '\n')
#
#
# # 1~10까지 list 에 담은 후 짝수만 출력
# li3 = list(range(1, 11))
# for i in li3:
#     if i % 2 == 0:
#         print(i , end =' ')
# print()
#
# number_list = []
# for i in range(10):
#     number_list.append(i + 1)
#
# for i in range(len(number_list)):
#     if number_list[i] % 2 == 0:
#         print(number_list[i], end = ' ')
# print()
#
# # 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# li4 = ['짱구', '훈이', '맹구', '유리']
# print("초기 li4 값: {}".format(li4))
# li4[1] = '철수'
# print("변경 후 li4 값: {}".format(li4))
# # li4.remove(li4[-1])
# del li4[-1]
# print("삭제 후 li4 값: {}".format(li4))

# list안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
# print(number_list[0][1])

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])


# length = len(number_list) * len(number_list[0])
# for i in range(length):
#     print(number_list[i // 3][i % 3])
