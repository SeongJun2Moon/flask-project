"""
이름, 주민번호 (950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
"""
from util.common import Common


class Person(object):
    def __init__(self, name, rrn, adrr) -> None:
        self.name = name
        self.rrn = rrn
        self.adrr = adrr

    def __str__(self):
            who = int(self.rrn.split("-")[0][:2])
            if who >= 22 and who < 100:
                age = 122 - who + 1
            else: age = 22 - who + 1
            who2 = int(self.rrn.split("-")[1][0])
            if who2 == 1 or who2 == 3:
                gen = "남자"
            else: gen = "여자"
            return f"{self.name} {age} {gen} {self.adrr}"

    @staticmethod
    def new_person():
        name = input("이름: ")
        rrn = input("주민등록번호: ")
        adrr = input("주소: ")
        return Person(name, rrn, adrr)

    @staticmethod
    def print_peaple(ls):
        print("### 회원 명부 ###\n******************************\n이름 나이 성별 주소\n******************************")
        [print(i) for i in ls]
        print("******************************")

    @staticmethod
    def delete_person(ls, name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]
