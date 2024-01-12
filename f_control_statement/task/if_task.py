# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.

message = "1. 빨간색\n2. 검은색\n3. 노란색\n4. 흰색\n위의 메뉴중 번호를 입력하세요: "
number = int(input(message))
choice_number = f"{number}번을 선택하셨습니다."
choice1, choice2, choice3, choice4 = number == 1, number == 2, number == 3, number == 4
color = None

if choice1:
    color = "색상은 red 입니다"
elif choice2:
    color = "색상은 black 입니다"
elif choice3:
    color = "색상은 yellow 입니다"
elif choice4:
    color = "색상은 while 입니다"

print(choice_number + color)