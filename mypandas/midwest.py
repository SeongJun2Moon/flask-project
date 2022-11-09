import pandas as pd
MENUS = [["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]]
MID = pd.read_csv("save/midwest.csv")


if __name__ == '__main__':
    while True:
        [print(f"{i}:{j}") for i, j in enumerate(MENUS)]
        menu = input("메뉴 선택: ")

        if menu == "0":
            print("종료")
            quit()
        elif menu == "1":
            print(f"{MID.head()}\n{MID.tail()}\n{MID.shape}\n{MID.info()}\n{MID.describe()}")
        elif menu == "2":
            total = None
