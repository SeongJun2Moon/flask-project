from dataclasses import dataclass


@dataclass
class OOP:
    x = 30

    def foo(self):
        x = self.x
        print("OOP 출력: " + str(x))


x = 110


def foo():
    global x
    x = x + 20
    print("FP 출력: " + str(x))


def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            global x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()


def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + (a * x + b)
        print(total)
    def mul_add2(x):
        nonlocal total
        total = total + (a * x - b)
        return print(total)
    return {'mul_add': mul_add, 'mul_add2': mul_add2}
    # 클로저 = 함수 안에 함수 호출하기


def clac_lambda():
    a = 3
    b = 5
    return lambda x: a * x + b
    # 람다로 클로저

if __name__ == '__main__':
    f = OOP()
    f.foo()
    foo()
    print("전역출력: " + str(x))

    A()

    calc()['mul_add'](1)
    calc()['mul_add2'](1)

    c = clac_lambda()
    print(clac_lambda()(1), clac_lambda()(2))