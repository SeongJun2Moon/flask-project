from canny.views import MenuController
from util.common import Common
LENNA = "Lenna.png"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
line = "http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
HAAR = "haarcascade_frontalface_alt.xml"
GIRL = "girl.jpg"
GIRL_SIDE = ""
FAMILY = "family"
CAT = "cat.jpg"
GIRL_TURN = ""
if __name__ == '__main__':
    api = MenuController()
    while True:
        menus = ["종료", "원본보기", "그레이스케일", "엣지검출", "직선검출", "얼굴-모자이크", "얼굴인식", "모자이크", "얼굴추출"]
        menu = Common.menu(menus)

        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1": api.menu_1(menus[1], LENNA)
        elif menu == "2": api.menu_2(menus[2], SOCCER)
        elif menu == "3": api.menu_3(menus[3], SOCCER)
        elif menu == "4": api.menu_4(menus[4], line)
        elif menu == "5": api.menu_5(menus[5], HAAR, GIRL)
        elif menu == "6": api.menu_6(menus[6], CAT, HAAR)
        else:
            print(" ### 해당 메뉴 없음 ### ")
