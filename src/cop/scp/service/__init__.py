from src.cop.scp.service.domains import Scrap
from src.cop.scp.service.view import ScrapController

if __name__ == '__main__':
    api = ScrapController()
    scrap = Scrap()
    while True:
        menus = ["종료", "벅스뮤직", "멜론뮤직"]
        menu = input("메뉴 선택: ")

        if menu == "0":
            api.menu_0()
            break
        elif menu == "1":
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total"
            scrap.query_string = "?chartdate=20221106"
            scrap.parser = "lxml"
            scrap.class_names = ["title", "artist"]
            scrap.tag_name = 'p'
            api.menu_1(scrap)
        elif menu == "2":
            scrap.domain = "https://www.melon.com/chart/index.htm"
            scrap.query_string = "?dayTime=2022110909"
            scrap.parser = "lxml"
            scrap.class_names = ["rank01", "rank02"]
            scrap.tag_name = 'div'
            api.menu_2(scrap)
        else:
            print(" ### 해당 메뉴 없음 ### ")
