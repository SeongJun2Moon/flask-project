"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
유관순 90 90 92 272 90.6 A
********************************
"""

class Grade(object):
    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma

    def print(self):
        print(f"{self.name} {self.ko} {self.en} {self.ma}")

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def print_grade(ls):
        print("### 성적표 ###\n********************************\n이름 국어 영어 수학 총점 평균 학점\n*******************************")
        for i in ls:
            i.print()
        print("********************************")

    @staticmethod
    def new_grade():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        print("등록 완료")
        return Grade(name, ko, en, ma)

    @staticmethod
    def print_menu():
        print("1.성적등록\n2.성적조회\n3.성적삭제\n4.종료")
        return int(input("메뉴선택: "))

    @staticmethod
    def main():
        lst = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                lst.append(Grade.new_grade())
            elif menu == 2:
                Grade.print_grade(lst)
            elif menu == 3:
                Grade.delete_grade(lst, input("삭제할 이름: "))
            elif menu == 4:
                print("종료")
                break
            else: print("그런거 없음")

Grade.main()