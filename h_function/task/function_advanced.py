# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

def select_by_price(price, range=50):
    result = []
    min = price * range * 0.01
    max = price * (range * 0.01 + 1)

    for name, price in data_dict.items():
        if min <= price <= max:
            result.append({"name": name, 'price':price})
    return result
# ====
    # 추가
def append(**kwargs):
    if kwargs.get('name') not in [i for i in data_dict.keys()]:
        data_dict[kwargs.get('name')] = kwargs.get('price')
    else:
        print(append_error_message)

# ===
    # 수정
def update(name):
    if name in [i for i in data_dict.keys()]:
        update_name, update_price = input(update_message).split()
        if name == update_name:
            data_dict[update_name] = update_price
        else:
            print(update_error_message2)
    else:
        print(update_error_message1)

# ===
    # 삭제
def delete(name):
    if name in [i for i in data_dict.keys()]:
        del data_dict[name]
    else:
        print(delete_error_message)


while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split()
        append(name=new_name, price=new_price)

    # 수정
    elif choice == 2:

        name = input(search_name_message_for_update)
        update(name)

    # 삭제
    elif choice == 3:
        name = input(delete_message)
        delete(name)


    # 검색
    elif choice == 4:
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            keyword = input(search_name_message)
            if keyword in data_dict:
                for name, price in data_dict.items():
                    if keyword == name:
                        print(f'{name}, {price}')
                continue

            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            price_input = int(input(search_price_message))
            result = select_by_price(price_input)

            if len(result) != 0:
                for product in result:
                    print(f"{product.get('name')}, {product.get('price')}")
                continue

            else:
                result_message = search_error_message

    # 목록
    elif choice == 5:
        if len(data_dict) == 0:
            result_message = no_item_message
        else:
            for name, price in data_dict.items():
                print(f'{name}, {price}')
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        result_message = error_message

    print(result_message)
    result_message = ""






