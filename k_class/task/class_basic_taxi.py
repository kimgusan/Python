# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 잔돈 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi:

    default_chargs = 5800
    default_distance = 2
    taxi_pay = 1000
    # revenue = 0


    def __init__(self, money, distance):
        self.money = money
        self.distance = distance
        self.revenue = 0

    def pay(self):
        if self.distance <= Taxi.default_distance:
            return f"승객이 내야할 돈은 {Taxi.default_chargs}입니다"
        else:
            return f"승객이 내야할 돈은 {Taxi.default_chargs + ((self.distance - 2) * (Taxi.taxi_pay))}입니다"

    def get_chargs(self):
        if self.distance <= Taxi.default_distance:
            return f"택시기사가 줄 잔돈은 {self.money - Taxi.default_chargs}입니다"
        else:
            return f"택시기사가 줄 잔돈은 {self.money - (Taxi.default_chargs + (self.distance - 2) * (Taxi.taxi_pay))}입니다"


taxi1= Taxi(10000,3)
taxi2= Taxi(20000,4)

print(taxi1.pay())
print(taxi1.get_chargs())
print(taxi2.pay())
print(taxi2.get_chargs())