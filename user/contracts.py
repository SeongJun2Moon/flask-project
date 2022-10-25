'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''
from util.common import Common


class Contracts(object):
    def __init__(self, name, num, mail, adrr) -> None:
        self.name = name
        self.num = num
        self.mail = mail
        self.adrr = adrr

    def __str__(self):
        return f"{self.name} {self.num} {self.mail} {self.adrr}"

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
        [print(i) for i in ls]
        print("******************************")

    @staticmethod
    def delete_contract(ls,name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]
