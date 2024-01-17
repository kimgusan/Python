# [종합 실습]
# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고

# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막
#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
def check(key, value):
    for banks in Bank.bank_list:
        for bank in banks:
            if bank.get(key) == value:
                return bank

        # return None
        return print('hello')



class Bank:
    total_count = 3
    bank_list = [[] for i in range(total_count)]

    def __init__(self, **kwargs):
        '''
        :param kwargs: name=예금주, account= 계좌번호, phone_number= 전화번호, password=비밀번호, account_money=계좌잔액
        '''
        self.object = self
        self.name = kwargs.get('name')
        self.account = kwargs.get('account')
        self.phone_number = kwargs.get('phone_number')
        self.password = kwargs.get('password')
        self.account_money = kwargs.get('account_money')

    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        bank_name = [SinHan, KookMin, Kakao][bank_choice - 1](**kwargs)  # 나는 선언을 하고 끝난거지. 여기서 어떤 은행이든 객체화를 시켜버리고 끝
        user_list = {'name': kwargs.get('name'),
                     'account': kwargs.get('account'),
                     'phone_number': kwargs.get('phone_number'),
                     'password': kwargs.get('password'),
                     'account_money': kwargs.get('account_money')
                     }
        Bank.bank_list[bank_choice - 1].append(user_list)
        return bank_name

    @staticmethod
    def check_account_number(account_number):
        return check(key="account_number", value=account_number)

    @staticmethod
    def check_phone_number(phone_number):
        return check(key="phone_number", value=phone_number)

    def deposit(self, money):  # 입금시 어떤 계좌에 얼마를 입금할껀지 알아야 하기 때문에 해당 매개변수 2개를 입력받아야 함
        self.account_money += money

    def withdraw(self, money):
        self.account_money -= money

    def balance(self):
        return self.account_money

    def __str__(self):
        pass


class SinHan(Bank):
    def __init__(self, **kwargs):
        pass

    def deposit(self, money):
        money //= 2
        super().deposit(money)


class KookMin(Bank):
    def withdraw(self, money):
        money *= 1.5
        super().withdraw(int(money))


class Kakao(Bank):
    def balance(self):
        self.account_money //= 2
        return super().balance()


if __name__ == '__main__':  # 현재 스크립트에서 모듈로 실행시키기 위한 관용구
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

while True:
    bank_choice = int(input(bank_menu))
    if bank_choice == 4:
        break
    elif bank_choice >= 5:
        continue
    while True:
        service_menu = int(input(menu))
        if service_menu == 5:
            break
        elif service_menu >= 6:
            print(error_message)
        elif service_menu == 1:
            name = input(owner_message)
            while True:
                account_number = input(account_number_message)
                if Bank.check_account_number is not None:
                    break
            while True:
                phone_number = input(phone_message)
                if Bank.check_phone_number is not None:
                    break
            while True:
                password = input(password_message)
                if len(password) == 4:
                    break
            account_money = int(input(money_message))

            user = Bank.open_account(bank_choice=bank_choice, name=name, account=account_number,
                                     phone_number=phone_number, password=password, account_money=account_money)

        elif service_menu == 2:
            pass
        elif service_menu == 3:
            pass
        elif service_menu == 4:
            account_number = input(account_number_message)
            user = Bank.check_account_number(account_number)
            print(user)
            # if user is not None:
            #     if user.get('password') == input(password_message):
            #         print(user.get('object').balance())
            #         continue
            # else:
            #     None