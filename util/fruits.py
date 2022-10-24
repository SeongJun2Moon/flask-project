"""
과일판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
다만, 실행했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
구매할 과일: 바
"""

class Fruits(object):
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount

    def print(self):
        print(f"{self.name} {self.amount}")

    @staticmethod
    def print_menu():
        print("1.과일등록 2.과일조회 3.과일삭제 4.종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def new_fruit():
        name = input("과일 이름: ")
        amount = int(input("과일 수량: "))
        return Fruits(name, amount)

    @staticmethod
    def print_fruits(ls):
        print("### 과일들 ###\n******************************\n과일 수량\n******************************")
        for i in ls:
            i.print()
        print("******************************")

    @staticmethod
    def delete_fruit(ls, name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Fruits.print_menu()
            if menu == 1:
                ls.append(Fruits.new_fruit())
            elif menu == 2:
                Fruits.print_fruits(ls)
            elif menu == 3:
                Fruits.delete_fruit(ls, input("삭제할 과일: "))
            elif menu == 4:
                print("종료")
                break
            else: print("그런거 없음")

Fruits.main()

