'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
'''
from util.common import Common


class Member(object):

    def __init__(self, id, pw, name)->None:
        self.id = id
        self.pw = pw
        self.name = name

    def __str__(self):
        return f"{self.id} {self.pw} {self.name}"

    @staticmethod
    def new_member():
        id = input("아이디: ")
        pw = input("비밀번호: ")
        name = input("이름: ")
        return Member(id, pw, name)

    @staticmethod
    def print_members(ls):
        print("### 회원명부 ###\n******************************\n아이디 비밀번호 이름\n******************************")
        [print(i) for i in ls]
        print("******************************")

    @staticmethod
    def delete_member(ls, name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 1:
                ls.append(Member.new_member())
            elif menu == 2:
                Member.print_members(ls)
            elif menu == 3:
                Member.delete_member(ls, input("삭제할 이름: "))
            elif menu == 4:
                print("4")
                break
            else : print("그런거 없음")

Member.main()