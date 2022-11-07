from scrapper.domains import MusicRanking
from scrapper.view import MenuController

if __name__ == '__main__':
    api = MenuController()
    m = MusicRanking()
    while True:
        menus = ["종료", "벅스뮤직", "멜론뮤직"]
        menu = input("메뉴 선택: ")

        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            m.domain = "https://music.bugs.co.kr/chart/track/day/total"
            m.query_string = "20221106"
            m.parser = "lxml"
            m.class_names = ["title", "artist"]
            m.tag_name = 'p'
            api.menu_1('m')
        elif menu == "2":
            api.menu_2("https://www.melon.com/chart/index.htm")
        else:
            print(" ### 해당 메뉴 없음 ### ")
