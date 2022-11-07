from util.common import Common
from scrapper.view import MenuController

if __name__ == '__main__':
    api = MenuController
    while True:
        menus = ["종료", "벅스뮤직", "멜론뮤직"]
        menu = input("메뉴 선택: ")

        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            api.menu_1("https://music.bugs.co.kr/chart/track/day/total")
        elif menu == "2":
            api.menu_2("https://www.melon.com/chart/index.htm")
        else:
            print(" ### 해당 메뉴 없음 ### ")
