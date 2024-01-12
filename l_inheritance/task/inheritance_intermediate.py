# [종합 실습]
# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
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


def check():
    pass

x
class Bank:
    total_count = 3
    banks = [[] for bank in range(total_count)] # [[]]

    def __init__(self):
        pass

    @classmethod
    def open_account(cls,bank_number, name, account, phone, password, balance= 0):
        cls.bank_number = bank_number
        cls.name = name
        cls.account = account
        cls.phone = phone
        cls.password = password
        cls.balance = balance
        cls.banks[bank_number-1].append({'name': name, 'account': account, 'phone': phone, 'password':password, 'balance': balance})
        print(cls.banks)

    @staticmethod
    def check_account_number():
        check()

    @staticmethod
    def check_phone():
        check()

    def deposit(self, bank_number, account, balance): # 어떤 계좌에 얼마를 입급할까?
        self.bank_number = bank_number
        self.account = account
        self.balance = balance
        for bank in Bank.banks[bank_number-1]:
            if bank['account'] == self.account:
                bank['balance'] += self.balance


    def withdraw(self):
        pass

    def balance(self):
        pass

    def __str__(self):
        pass


class ShinHan(Bank):
    def open_account(self, bank_number, name, account, phone, password, balance=0):
        super().open_account(bank_number, name, account, phone, password, balance)
        self.balance = 0


    def deposit(self, bank_number, account, balance):
        super().deposit(bank_number, account, balance)


class KookMin(Bank):
    def open_account(self, bank_number, name, account, phone, password, balance=0):
        super().open_account(bank_number, name, account, phone, password, balance=0)


class KaKao(Bank):
    def open_account(self, bank_number, name, account, phone, password, balance=0):
        super().open_account(bank_number, name, account, phone, password, balance=0)


if __name__ == '__main__':
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
    # 은행 메뉴
    bank_number = int(input(bank_menu))
    if bank_number == 1:
        shinhan = ShinHan()

    elif bank_number == 2:
        kookmin = KookMin()
    elif bank_number == 3:
        kakao = KaKao()
    elif bank_number == 4:
        break
    else:
        print(error_message)

    while True:
        # 서비스 메뉴
        service_number = int(input(menu))
        if service_number == 1: # 계좌 개설
            name = input(owner_message)
            account = input(account_number_message)
            phone = int(input(phone_message))
            password = input(password_message)
            balance = int(input(money_message))

            if bank_number == 1:
                shinhan.open_account(bank_number, name, account, phone, password, balance)
            elif bank_number == 2:
                kookmin.open_account(bank_number, name, account, phone, password, balance)

            elif bank_number == 3:
                kakao.open_account(bank_number, name, account, phone, password, balance)

        elif service_number == 2: # 입금
            name = input(owner_message)
            account = input(account_number_message)
            balance = int(input(deposit_message))
            shinhan.deposit(bank_number, account, balance)


        elif service_number == 3:
            pass
        elif service_number == 4:
            pass
        elif service_number == 5:
            break
        else:
            print(error_message)





