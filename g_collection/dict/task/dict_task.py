# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
# ~~~ 완료 후 주석달기~~~~~
data_dict = {}

title = "과일가게"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n" # 검색과 관련된 내용
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격' #추가와 관련된 내용
search_name_message_for_update = '수정하실 상품명을 입력하세요.' #수정과 관련된 내용
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격' #수정과 관련된 내용
delete_message = '삭제하실 상품명을 입력하세요.' # 삭제와 관련된 내용
search_name_message, search_price_message = '상품명: ', '가격: ' #검색과 관련된 내용

append_error_message = "추가 실패(중복된 상품명)" # 추가
update_error_message = "수정 실패(존재하지 않는 상품명)" # 수정
delete_error_message = "삭제 실패(존재하지 않는 상품명)" # 삭제
search_name_error_message = "검색 실패(존재하지 않는 상품명)" #검색
search_error_message = "검색 결과가 없습니다." #검색
price_search_error_message = "검색 결과가 없습니다." #검색
error_message = "다시 입력해주세요." # 수정, 삭제, 검색
no_item_message = "목록이 없습니다." #검색

error_result = ""  #반복 출력을 최소화 하기 위하여 일괄처리를 하기 위해 문자열 빈 변수 생성

while True:
    # 사용자에게 입력받는 choice 저장공간생성 및 정수 형변환
    choice = int(input(title + "\n" + menu))

    # 사용자가 1번을 선택하였을 때
    if choice == 1:
        # 입력함수를 사용하여 사용자에게 값 입력 받기, split() 함수를 통한 변수 2개 입력 받기
        new_name, new_price = input(append_message).split()
        # 오차 범위를 확인하기 위해 정수 형변환
        new_price = int(new_price)
        # 사용자에게 입력받은 new_name 값이 name_list 에 존재하지 않는 경우
        if new_name not in data_dict.keys():
            # name_list, price_list에 사용자에게 입력받은 값 대입
            data_dict[new_name] = new_price
            # 오류 메세지를 출력하지 않기 위해 continue 사용
            continue
        # 만약 사용자에게 입력받은 값이 name_list 에 존재하는 경우
        else:
            # 에러 메세지를 변수에 대입
            error_result = append_error_message

    # 사용자가 1번을 선택하지 않고 2번을 선택하였을 때
    elif choice == 2:
        # 사용자가 수정하고 싶은 이름 변수 대입
        re_name = input(search_name_message_for_update)
        # 사용자가 수정하고 싶은 요소가 name_list 에 이미 존재한다면
        if re_name in data_dict.keys():
            # 사용자가 바꾸고 싶은 새로운 이름과 바꾸고 싶은 금액을 한줄로 입력받기
            new_name, new_price = input(update_message).split()
            # new_price = int(new_price) 불필요한 코드
            # 기존에 사용자가 수정하고 싶었던 요소의 인덱스 값 확인 및 변수 대입
            # 신규로 사용자가 바꾸고 싶은 각각의 요소를 기존 name_list, price_list 인덱스 위치에 대입
            data_dict[new_name] = new_price
            # 오류 메세지를 출력하지 않기 위해 continue 사용
            continue
        # 사용자가 수정하고 싶은 요소가 name_list에 존재하지 않는다면
        else:
            # 에러 메세지를 변수에 대입
            error_result = update_error_message

    # 사용자가 1,2 번을 선택하지 않고 3번을 선택하였을 때
    elif choice == 3:
        # 사용자가 삭제하고 싶은 요소 입력 받아 변수 대입
        d_name = input(delete_message)
        # 사용자가 삭제하고 싶은 요소가 name_list 에 존재하는 경우
        if d_name in data_dict.keys():
            # 해당 name_list에 인덱스 번호 확인 및 index 변수 대입
            # 해당 인덱스 번호의 위치의 요소 값 삭제
            del data_dict[d_name]
            # 오류 메세지를 출력하지 않기 위해 continue 사용
            continue
        # 사용자가 삭제하고 싶은 요소가 name_list에 존재하지 않는 경우
        else:
            # 에러 메세지를 변수 대입
            error_result = delete_error_message

    # 사용자가 1,2,3 번을 선택하지 않고 4번을 선택하였을 때
    elif choice == 4:
        # 사용자가 검색 기준을 어떤 것으로 정할 지 변수 대입
        menu_choice = int(input(search_menu))
        # 사용자가 검색 기준을 이름으로 했을 때
        if menu_choice == 1:
            # 사용자가 검색하고 싶은 요소를 입력받아 변수 대입
            search_name = input(search_name_message)
            # 사용자가 검색하고 싶은 요소가 name_list에 존재하는 경우
            if search_name in data_dict.keys():
                # 해당 리스트 전체와 사용자가 입력한 요소 출력
                print(f"{data_dict.keys()} 안에 {search_name}는 존재 합니다.")
                # 오류 메세지를 출력하지 않기 위해 continue 사용
                continue
            # 사용자가 검색하고 싶은 요소가 name_list에 존재하지 않는 경우
            else:
                # 에러 메세지에 검색하는 이름 요소가 없다는 변수 대입
                error_result = search_error_message
        # 사용자가 검색 기준을 값으로 했을 때
        elif menu_choice == 2:
            count_index = []
            # 사용자가 검색하고 싶은 값 요소를 입력받아 정수형으로 형변환
            search_price = int(input(search_price_message))
        # 사용자가 입력한 값의 오차범위 내에 있는 값을 넣은 빈 리스트 생성

            # price_list 요소 개수만큼 반복
            price = [i for i in data_dict.values()]
            for i in range(len(data_dict)):
                # price_list의 인덱스 값이 사용자에게 입력받은 최소값과 최대값 사이에 있는 경우
                if search_price * 0.5 <= price[i] <= search_price * 1.5:
                    # 빈 인덱스에 price_list 요소 값 추가
                    count_index.append(price[i])

            # count_index 리스트 개수의 값이 0이 아닌 경우
            if len(count_index) != 0:
                # count_index 리스트 값에 있는 요소 개수 출력
                print(f"count: {len(count_index)}")
                count_index.clear()
                # 오류 메세지를 출력하지 않기 위해 continue 사용
                continue
            # count_index 리스트 개수의 값이 0인 경우
            else:
                error_result = error_message

    # 사용자가 1,2,3,4 가 아닌 5번을 선택했을 때
    elif choice == 5:
        # name_list 의 요소의 개수가 0이 아닌 경우
        if len(data_dict) != 0:
            for key, values in data_dict.items():
                print(f"{key}, {values}")

            # 오류 메세지를 출력하지 않기 위해 continue 사용
            continue
        # 그 이외의 경우
        else:
            # 에러 메세지 변수 대입
            error_result = no_item_message

    # 사용자가 1,2,3,4,5 가 아닌 6을 선택 한 경우 반복문 종료
    elif choice == 6:
        break
    # 사용자가 1,2,3,4,5,6 숫자가 아닌 다른 숫자를 선택한 경우
    else:
        # 에레 메세지 변수 대입
        error_result = error_message

    # 상단의 if 구문에서 잘못된 에러 메세지가 입력되는 경우 에러 메세지 출력
    print(error_result)

