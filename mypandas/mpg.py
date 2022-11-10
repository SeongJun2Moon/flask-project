import numpy as np
import pandas as pd
import dataframe_image as dfi
from matplotlib import pyplot as plt

my_meta = {
    "manufacturer": "회사",
    "model": "모델",
    "displ": "배기량",
    "year": "연식",
    "cyl": "실린더",
    "trans": "차축",
    "drv": "오토",
    "cty": "시내연비",
    "hwy": "시외연비",
    "fl": "연료",
    "class": "차종"
}


MENUS = ["종료", "앞부분 확인", "뒷부분 확인", "행열출력", "데이터속성 확인", "요약 통계량 출력", "문자 변수 요약 통계량 함께 출력",
         "manufacturer 를 company 로 변경", "test 변수 생성",
         # cty 와 hwy 변수를 merge 하여 total, 변수 생성하고 20이상이면 pass 미만이면 fail 저장
         "test 빈도표 만들기", "test 빈도 막대 그래프 그리기",
        # mpg 144페이지 문제
         "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
         "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
         "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
        # mpg 150페이지 문제
        # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
        # 후 다음 문제 풀이
        "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?",
        # mpg 153페이지 문제
        "아우디차에서 고속도로 연비 1~5위 출력하시오",
        # mpg 158페이지 문제
        "평균연비가 가장 높은 자동차 1~3위 출력하시오"
         ]
MPG = pd.read_csv("save/mpg.csv")

class Mpg:

    def __init__(self):
        self.mpg = MPG
        self.mpg_test = None
        self.chart = None

    def head(self): #1
        print(self.mpg.head())

    def tail(self): #2
        print(self.mpg.tail())

    def shape(self): #3
        print(self.mpg.shape)

    def info(self): #4
        print(self.mpg.info())

    def describe(self): #5
        print(self.mpg.describe())

    def describe2(self): #6
        print(self.mpg.describe(include='all'))

    def change_meta(self): #7
        self.mpg_test = self.mpg.rename(columns=my_meta)

    def create_test(self): #8
        self.change_meta()
        t = self.mpg_test
        t["종합연비"] = (t['시내연비'] + t['시외연비']) / 2
        t['연비테스트'] = np.where(t['종합연비'] >= 20, "pass", "fail")
        self.mpg_test = t

    def create_test_frequency(self): #9
        self.create_test()
        t = self.mpg_test
        count_test = t['연비테스트'].value_counts()
        self.chart = count_test

    def create_test_grape(self): # 10
        self.create_test_frequency()
        chart = self.chart
        chart.plot.bar(rot = 0)
        plt.savefig('./save/mpg_graph.png')

    def displ_hwy(self): #11
        self.create_test()
        print("\ndispl(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교")
        print(f'4이하 평균: {self.mpg_test.query("displ <= 4")["hwy"].mean()}\n5이상 평균: {self.mpg_test.query("displ >= 5")["hwy"].mean()}\n')

    def audi_toyota(self): #12
        print(self.mpg.query("manufacturer == 'audi'")['cty'].mean())
        print(self.mpg.query("manufacturer == 'toyota'")['cty'].mean())

    def car3(self): #13
        print(self.mpg.query("manufacturer in ['chevrolet', 'ford', 'honda']"))
        print(f"hwy평균: {self.mpg['hwy'].mean()}\n")

    def suv_compact(self): #14
        self.change_meta()
        compact = self.mpg_test.query("차종 == 'compact'")['시외연비'].mean()
        suv = self.mpg_test.query("차종 == 'suv'")['시외연비'].mean()
        print(f"compact연비: {compact}\nsuv연비: {suv}\n")


    def audi_hwy(self): #15
        self.change_meta()
        print(self.mpg_test.query("회사 == 'audi'").sort_values('시외연비').head())

    def hwy_avg(self):
        self.create_test()
        chart = self.mpg_test
        print(chart.sort_values("종합연비", ascending=False).head(3))


if __name__ == '__main__':
    t = Mpg()
    while True:
        [print(f"{i}:{j}") for i, j in enumerate(MENUS)]
        menu = input("메뉴 선택: ")

        if menu == "0":
            print("종료")
            quit()
        elif menu == "1":
            print("앞부분 확인")
            t.head()
        elif menu == "2":
            print("뒷부분 확인")
            t.tail()
        elif menu == "3":
            print("행열출력")
            t.shape()
        elif menu == "4":
            print("데이터속성 확인")
            t.info()
        elif menu == "5":
            print("요약 통계량 출력")
            t.describe()
        elif menu == "6":
            print("문자 변수 요약 통계량 함께 출력")
            t.describe2()
        elif menu == "7":
            print("manufacturer 를 company 로 변경")
            t.change_meta()
        elif menu == "8":
            print("test 변수 생성")
            t.create_test()
        elif menu == "9":
            print("test 빈도표 만들기")
            t.create_test_frequency()
        elif menu == "10":
            print("test 빈도 막대 그래프 그리기")
            t.create_test_grape()
        elif menu == "11":
            t.displ_hwy()
        elif menu == "12":
            print("\n아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색")
            t.audi_toyota()
        elif menu == "13":
            print("\n쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균")
            t.car3()
        elif menu == "14":
            print("\nsuv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?\n")
            t.suv_compact()
        elif menu == "15":
            print("\n아우디차에서 고속도로 연비 1~5위 출력하시오")
            t.audi_hwy()
        elif menu == "16":
            t.hwy_avg()
            print("\n평균연비가 가장 높은 자동차 1~3위 출력하시오")

