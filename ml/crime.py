import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CRIME_MENUS = ["종료", #0
            "데이터구조파악",#1
            "연속형변수편집",#2
            "범주형변수편집",#3
            "샘플링",#4
            "학습",#5
            "예측"]#6

crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.ordinal(),
    "3" : lambda t: t.norminal(),
    "4" : lambda t: t.interval(),
    "5" : lambda t: t.ratio(),
    "6" : lambda t: t.partition()
}

class Crime:

    def __init__(self):
        self.crime = pd.read_csv("data/crime_in_seoul.csv")
        self.cctv = pd.read_csv("data/cctv_in_seoul.csv")

    def temp(self):
        return lambda x: print(f" --- 1.Shape ---\n{x.shape}\n"
                               f" --- 2.Features ---\n{x.columns}\n"
                               f" --- 3.Info ---\n{x.info()}\n"
                               f" --- 4.Case Top1 ---\n{x.head(3)}\n"
                               f" --- 5.describe ---\n{x.describe()}\n")

    def spec(self):
        print(" --- 클로저 테스트 ---")
        [self.temp()(i) for i in [self.crime, self.cctv]]

    def ordinal(self):
        pass

    def norminal(self):
        pass

    def interval(self):
        pass

    def ratio(self):
        pass

    def partition(self):
        pass

if __name__ == '__main__':
    Crime().spec()