# # 1~15까지 출력
# for i in range(15):
#     print(i + 1, end = ' ')
# print()
#
# # 30~1 까지 출력
# for i in range(30):
#     print(30 - i, end=' ')
# print()
#
# # 1~100 까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1, end=' ')
# print()
#
# # 1~10까지 합 출력
# sum = 0
# for i in range(10):
#     sum += i + 1
# print(sum)
#
# # 1~n까지 합 출력
# message = "정수를 입력하세요: "
# n = int(input(message))
# total = 0
# for i in range(n):
#     total += i + 1
# print(f"1부터 {n}까지의 합은 {total}입니다")
#
# # 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(3):
#     for j in range(3, 7):
#         print(j, end=' ')
#     print(end='')
# print()
#
# # for 구문을 1번 사용해서 출력 , 규칙성이 있으면 나머지 연산을 사용
# for i in range(12):
#     print(i % 4 + 3, end = ' ')
# print()
#
# # '1,235,500'를 1235500으로 출력
# data = '1,235,500'
# result = ''
# for i in data:
#     if i != ',':
#         result += i
#
# result = int(result)
# print(result)

# 1~10까지 중 3까지만 출력
# for i in range(10):
#     print(i + 1)
#     if i == 2:
#         break

# 1~10까지 중 4를 제외하고 출력
for i in range(10):
    if i == 3:
        continue
    print(i + 1)

