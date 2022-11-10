import pandas as pd
import numpy as np

MENUS = ["종료", "과일2D", "숫자2D"]
def new_fruites_df():
    ls_schema = ['제품', '가격', '판매량'] # 스키마
    l1 = ["사과", "딸기", "수박"]
    l2 = [1800, 1500, 3000]
    l3 = [24, 38, 13]
    ls_apd = [l1, l2, l3]
    dc = {j : ls_apd[i] for i,j in enumerate(ls_schema)}
    df = pd.DataFrame(dc)
    return df


def my_list(a, b):
    return list(range(a, b))


def new_number_2d(): # 딕셔너리 없이 데이터프레임 만들기
    return pd.DataFrame(np.array([my_list(1,10), my_list(11, 20), my_list(21, 30)]), columns=list(map(chr, range(97, 107))))
                                                                                                # 아스키코드 사용


if __name__ == '__main__':
    while True:
        [print(f"{i}:{j}") for i, j in enumerate(MENUS)]
        menu = input("메뉴 선택: ")

        if menu == "0":
            print(MENUS[0])
            quit()
        elif menu == "1":
            print(MENUS[1])
            print(new_fruites_df())
        elif menu == "2":
            print(MENUS[2])
            print(new_number_2d())


