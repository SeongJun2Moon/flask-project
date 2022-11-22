class Calculator(object):
    def __init__(self, num1, op, num2) -> None:
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def print(self):
        if self.op == "+":
            print(f"{self.num1}{self.op}{self.num2} = {self.num1+self.num2} ")
        elif self.op == "-":
            print(f"{self.num1}{self.op}{self.num2} = {self.num1-self.num2} ")
        elif self.op == "*":
            print(f"{self.num1}{self.op}{self.num2} = {self.num1*self.num2} ")
        elif self.op == "/":
            print(f"{self.num1}{self.op}{self.num2} = {self.num1/self.num2} ")
        elif self.op == "%":
            print(f"{self.num1}{self.op}{self.num2} = {self.num1%self.num2} ")
        else:print("그런거 없음")

    @staticmethod
    def main():
        num1 = int(input("숫자1: "))
        op = input("+ - * / %: ")
        num2 = int(input("숫자2: "))
        cal = Calculator(num1, op, num2)
        cal.print()

Calculator.main()