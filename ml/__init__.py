from ml.stroke import STROKE_MENUS, stroke_menu
from ml.stroke import StrokeService
from ml.crime import Crime


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Crime()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            t.spec()
        elif menu == '2':
            t.save_police_pos()
        elif menu == '3':
            t.save_cctv_pos()
        elif menu == '4':
            t.save_police_norm()
        elif menu == '5':
            t.folium_example()
        elif menu == '6':
            t.sampling()
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")