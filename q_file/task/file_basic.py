# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면 ,fish.txt의 전체 내용을 삭제한다
# 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.

# 반복구문을 사용해볼 것

# with open('fish.txt', 'w', encoding='utf-8') as file:
#     fish_name = input("물고기를 입력하세요: ")
#     file.write(fish_name)
#
#
# input_str = input('fish.txt 파일 내용 전체 삭제 q 선택,\nfish.txt 파일 출력 r선택 : ')
# if input_str == 'q':
#     with open('fish.txt', 'w', encoding = 'utf-8') as file:
#         file.write('')
#         result = '삭제완료'
# elif input_str == 'r':
#     with open('fish.txt', 'r', encoding='utf-8') as file:
#         result = file.readline()
#
# print(result)

# 고등어를 참치로 수정하기

