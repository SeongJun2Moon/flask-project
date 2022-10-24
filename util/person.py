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

class Person(object):
    def __init__(self, name, rrn, adrr) -> None:
        self.name = name
        self.rrn = rrn
        self.adrr = adrr

    def print(self):
            who = int(self.rrn.split("-")[0][:2])
            if who >= 22 and who < 100:
                age = 122 - who + 1
            else: age = 22 - who + 1
            who2 = int(self.rrn.split("-")[1][0])
            if who2 == 1 or who2 == 3:
                gen = "남자"
            else: gen = "여자"
            print(f"{self.name} {age} {gen} {self.adrr}")

    @staticmethod
    def print_menu():
        print("1.회원등록 2.회원조회 3.회원삭제 4.종료")
        return int(input("메뉴선택: "))

    @staticmethod
    def new_person():
        name = input("이름: ")
        rrn = input("주민등록번호: ")
        adrr = input("주소: ")
        return Person(name, rrn, adrr)

    @staticmethod
    def print_peaple(ls):
        print("### 회원 명부 ###\n******************************\n이름 나이 성별 주소\n******************************")
        for i in ls:
            i.print()
        print("******************************")

    @staticmethod
    def delete_person(ls, name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 1:
                ls.append(Person.new_person())
            elif menu == 2:
                Person.print_peaple(ls)
            elif menu == 3:
                Person.delete_person(ls, input("삭제할 회원: "))
            elif menu == 4:
                print("종료")
                break
            else: print("그런거 없음")

Person.main()