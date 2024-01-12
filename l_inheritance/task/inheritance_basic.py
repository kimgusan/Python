# 인간 (부모)
# 이름, 나이

# 걷기 (walk)
# '두 발로 걷습니다.' 출력

# 원숭이(자식)
# 이름, 나이, 동물원 이름

# 걷기 (walk)
# '두 발로 걷습니다.', '네 발로 걷습니다.' 출력

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷습니다")

class Monkey(Human):
    def __init__(self, name, age, Zoo_name):
        super().__init__(name, age)
        self.Zoo_name = Zoo_name

    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')


monkey = Monkey('원숭이', '3살', '에버렌드')
monkey.walk()