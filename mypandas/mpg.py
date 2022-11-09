import pandas as pd
MENUS = ["종료", "앞부분 확인", "뒷부분 확인", "행열출력", "데이터속성 확인", "요약 통계량 출력", "문자 변수 요약 통계량 함께 출력"]
MPG = pd.read_csv("save/mpg.csv")

if __name__ == '__main__':

    while True:
        [print(f"{i}:{j}") for i, j in enumerate(MENUS)]
        menu = input("메뉴 선택: ")

        if menu == "0":
            print("종료")
            quit()
        elif menu == "1":
            print("앞부분 확인")
            print(MPG.head())
        elif menu == "2":
            print("뒷부분 확인")
            print(MPG.tail())
        elif menu == "3":
            print("행열출력")
            print(MPG.shape)
        elif menu == "4":
            print("데이터속성 확인")
            print(MPG.info())
        elif menu == "5":
            print("요약 통계량 출력")
            print(MPG.describe())
        elif menu == "6":
            print("문자 변수 요약 통계량 함께 출력")
            print(MPG.describe(include='all'))
