from ml.stroke import STROKE_MENUS, stroke_menu
from ml.stroke import StrokeService
from ml.oklahoma import okl_MENUS, okl_meta, okl_menu, Oklahoma


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            t.spec()
        elif menu == '2':
            t.rename_meta()
        elif menu == '3':
            t.target()
        elif menu == '4':
            t.interval_variables()
        elif menu == '5':
            t.nominal_variables()
        elif menu == '6':
            t.sampling()
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")