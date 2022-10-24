'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''

class Contracts(object):
    def __init__(self, name, num, mail, adrr) -> None:
        self.name = name
        self.num = num
        self.mail = mail
        self.adrr = adrr

    def print(self):
        print(f"{self.name} {self.num} {self.mail} {self.adrr}")

    @staticmethod
    def print_menu():
        print("1.연락처등록 2.연락처조회 3.연락처삭제 4.종료")
        return int(input("메뉴 선택: "))

    @staticmethod
    def new_contract():
        name = input("이름: ")
        num = input("전화번호: ")
        mail = input("이메일: ")
        adrr = input("주소: ")
        return Contracts(name, num, mail, adrr)

    @staticmethod
    def print_contracts(ls):
        print("### 연락처 ###\n******************************\n이름 전화번호 이메일 주소\n******************************")
        for i in ls:
            i.print()
        print("******************************")

    @staticmethod
    def delete_contract(ls,name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contracts.print_menu()
            if menu == 1:
                ls.append(Contracts.new_contract())
            elif menu == 2:
                Contracts.print_contracts(ls)
            elif menu == 3:
                Contracts.delete_contract(ls, input("삭제할 이름: "))
            elif menu == 4:
                print("종료")
                break
            else: print("그런거 없음")

Contracts.main()