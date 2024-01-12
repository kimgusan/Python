class A:

    @classmethod
    def __new__(cls, *args, **kwargs):     # 메모리에 기본으로 할당하는 기본 생성자 -> 생략해도 기본으로 생성
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data1, data2, name=''):                     # 사용자가 변수를 받아서 사용하는 생성자 라고 지칭 -> 생략해도 기본으로 생성
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)


# a = A()
a = A(10, 20, 'a')
print(a)
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()