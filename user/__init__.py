from user.bmi import Bmi
from user.contracts import Contracts
from user.grade import Grade
from user.person import Person
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료", "BMI", "주소록", "성적표", "개인 정보"])
    if menu == "0":
        print("### 앱 종료 ###")
        break
    if menu == "1":
        print("### BMI ###")
        submenu = Common.menu(["BMI등록", "BMI목록", "BMI삭제", "종료"])
        if submenu == "0":
            ls.append(Bmi.new_bmi())
        elif submenu == "1":
            Bmi.print_bmi(ls)
        elif submenu == "2":
            Bmi.delete_bmi(ls, input("삭제할 BMI: "))
        elif submenu == "3":
            print("종료")
            break
    elif menu == "2":
        print("### 주소록 ###")
        submenu = Common.menu(["주소록 등록", "주소록 목록", "주소록 삭제", "종료"])
        if submenu == 0:
            ls.append(Contracts.new_contract())
        elif submenu == 1:
            Contracts.print_contracts(ls)
        elif submenu == 2:
            Contracts.delete_contract(ls, input("삭제할 주소록: "))
        elif submenu == 3:
            print("종료")
            break
    elif menu == "3":
        print("### 성적표 ###")
        submenu = Common.menu(["성적표 등록", "성적표 목록", "성적표 삭제", "종료"])
        if submenu == 0:
            ls.append(Grade.new_grade())
        elif submenu == 1:
            Grade.print_grade(ls)
        elif submenu == 2:
            Grade.delete_grade(ls, input("삭제할 성적표이름: "))
        elif submenu == 3:
            print("종료")
            break
    elif menu == "4":
        print("### 개인정보 ###")
        submenu = Common.menu(["BMI등록", "BMI목록", "BMI삭제", "종료"])
        if submenu == 0:
            ls.append(Person.new_person())
        elif submenu == 1:
            Person.print_peaple(ls)
        elif submenu == 2:
            Person.delete_person(ls, input("삭제할 이름: "))
        elif submenu == 3:
            print("종료")
            break
    else: print("잘못된 메뉴 번호 입니다.")