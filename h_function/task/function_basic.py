# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

# ================================================================================================================
# <초기 로직 구성>
# 가. 매개변수 (pay, **coupon = %, **count = x)
# 나. 함수 내부에 if 조건문을 사용하여 count가 존재하는 경우 else: 존재하지 않는 경우 pay 에 할인된 값을 append 하여 리스트로 출력
# 다. if 조건 외부에 vm_total 빈 리스트 및 count, coupon 변수를 생성하여 입력된 값을 감소 시킬 수 있도록 가상의 값 추가
# 다-1. 쿠폰 개수를 감소시키기 위해 쿠폰을 지칭하는 변수 생성
# 다-2. 사용자가 값을 입력한 개수도 같이 감소 시키기 위해 pay 개수를 지칭하는 변수 생성
# 라. 반복 구문을 사용하여 pay의 길이만큼 반복
# 라-1. 만약 쿠폰이 1장 이상 있다면 할인율이 적용된 값을 vm_list 에 저장
# 라-2. 쿠폰 수량 1개 감소
# 라-3. 쿠폰이 수량이 줄어들어 쿠폰의 개수가 0보다 같거나 작아지면 나머지 pay 금액을 vm_list에 추가


def function_basic(pay, **kwargs):
    '''
    :param pay: 리스트로 입력받은 갚
    :param kwargs: coupon 할인율, count 값 입력
    '''
    vm_count = 0
    vm_coupon = 0
    vm_total = []
    if 'count' in kwargs:
        vm_count = kwargs['count']
        vm_coupon = kwargs['coupon']
        for i in range(len(pay)):
            if vm_count > 0:
                coupon_result = pay[i] * (1 - vm_coupon / 100)
                vm_total.append(int(coupon_result))
                vm_count -= 1
            else:
                vm_total.append(pay[i])
        return vm_total
    else:
        for i in pay:
            vm_total.append(pay[i])
        return vm_total

# print(function_basic([2000, 4000, 5000], coupon=50, count=2))
# print(function_basic([2000, 4000, 5000], coupon=50, count=2))
# print(function_basic([1000, 4000, 5000], coupon=30, count=100))


# ================================================================================================================
# <리팩토링 후 주석 달기>
# pay 리스트 매개변수 입력, keyward argument 값으로 coupon, count 값 입력
def coupon_discount(pay, **kwargs):
    '''
    :param pay: 리스트로 입력받은 갚
    :param kwargs: coupon 할인율, count 값 입력
    '''

    # 할인율을 적용하기 위한 딕셔너리 구조 value값 확인 및 수식 적용
    discount = (1-kwargs['coupon'] / 100)
    # 0부터 pay의 개수만큼 반복(len) 하되 리스트 컴프리핸션을 사용하여 조건절에 count의 값이 i+1 보다 큰 경우만 앞부분 i에 대입
    # 리스트 pay[i] 요소 확인 후 정수형으로 형변환
    # 해당 리스트 return

    return [int(pay[i] * discount) for i in range(len(pay)) if kwargs['count'] >= i+1]


print(coupon_discount([2000, 4000, 5000], coupon=50, count=3))
print(coupon_discount([2000, 4000, 5000], coupon=50, count=2))
print(coupon_discount([1000, 4000, 5000], coupon=30, count=100))





