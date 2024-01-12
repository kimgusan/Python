class A:
    def __init__(self, name):
        self.name = name
        print('부모생성자')

    def print_intro(self):
        print('A')



# tip.-- 자식생성자는 무조건 부모 생성자 먼저 호출된다
class B(A):
    def __init__(self, name):
        super().__init__(name) #부모 생성자
        print('자식생성자')

    def add(self, number1, number2):
        return number1 + number2

    def print_intro(self):
        # 부모의 메소드를 그대로 사용하고자 할 때
        super().print_intro()
        # 자식의 메소드에서 추가할 내용 작성
        print('B')

b = B('김규산')
print(b.name)
b.print_intro()
print(b.add(1,3))

