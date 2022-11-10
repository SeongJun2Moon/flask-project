import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MENUS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]
MID = pd.read_csv("save/midwest.csv")

class Mid:

    def __init__(self):
        self.mid = MID
        self.mid_rename = None

    def mid_features(self):
        mid = self.mid
        return f"{mid.head()}\n{mid.tail()}\n{mid.shape}\n{mid.info()}\n{mid.describe()}"

    def change_columns(self):
        self.mid_rename = self.mid.rename(columns = {"poptotal" : "total", "popasian" : "asian"})

    def create_asian_per(self):
        self.change_columns()
        mid = self.mid_rename
        mid["asian_per"] = ((mid["asian"] / mid["total"]) * 100)

    def asian_per_avg(self):
        self.create_asian_per()
        mid = self.mid_rename
        avg = mid["asian_per"].mean()
        mid["compare_per"] = np.where(mid["asian_per"] > avg, "large", "small")

    def compare_per_frequency(self):
        self.asian_per_avg()
        chart = self.mid_rename["compare_per"].value_counts()
        print(chart)
        chart.plot.bar(rot = 0)
        plt.savefig('./save/graph.png')

if __name__ == '__main__':
    mid = Mid()
    while True:
        [print(f"{i}:{j}") for i, j in enumerate(MENUS)]
        menu = input("메뉴 선택: ")

        if menu == "0":
            print("종료")
            quit()
        elif menu == "1":
            print(mid.mid_features())
        elif menu == "2":
            mid.change_columns()
        elif menu == "3":
            mid.create_asian_per()
        elif menu == "4":
            mid.asian_per_avg()
        elif menu == "5":
            mid.compare_per_frequency()
