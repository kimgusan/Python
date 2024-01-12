# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

class Product():
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        print(product_name, price)

class Market():
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell(self, customer):
        self.customer = customer
        discount_price =  self.product.price * (1 - customer.discount * 0.01)
        self.stock -= 1
        print(int(discount_price), self.stock)


class Customer():
    def __init__(self, name, age, discount, money):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money


product = Product('냉장고', 20000)
customer = Customer('alice', 20, 20, 10000)
market = Market(product, 40)
market.sell(customer)

