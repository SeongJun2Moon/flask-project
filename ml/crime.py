import googlemaps
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split
import pickle

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CRIME_MENUS = ["Exit", #0
            "Spec",#1
            "Merge",#2
            "Interval",#3
            "Norminal",#4
            "Ordinal",#5
            "Partition"]#6

crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pos(),
    "4" : lambda t: t.norminal(),
    "5" : lambda t: t.interval(),
    "6" : lambda t: t.ratio(),
    "7" : lambda t: t.partition()
}

class Crime:

    def __init__(self):
        self.crime = pd.read_csv("data/crime_in_seoul.csv")
        self.cctv = pd.read_csv("data/cctv_in_seoul.csv")
        self.pop = pd.read_excel("data/pop_in_seoul.xls", skiprows=[0, 2])[["자치구", "합계", "한국인", "등록외국인", "65세이상고령자"]]
        self.ls = [self.crime, self.cctv, self.pop]

    def spec(self):
        print(" --- 클로저 테스트 ---")
        [(lambda x: print(f" --- 1.Shape ---\n{x.shape}\n"
                               f" --- 2.Features ---\n{x.columns}\n"
                               f" --- 3.Info ---\n{x.info()}\n"
                               f" --- 4.Case Top1 ---\n{x.head(3)}\n"
                               f" --- 5.describe ---\n{x.describe()}\n"))(i)
         for i in self.ls]

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            # print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f"서울시내 경찰서는 총 {len(station_names)} 이다")
        # [print(f"{i}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("AIzaSyBgVssF55ids-IGxgRA0jx4-s2_2GoFxF8")
        # print(gmaps.geocode("서울종로경찰서", language='ko'))

        # print("API에서 주소추출 시작")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language="ko")
            # print(f'name:{i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get("formatted_address"))
            _loc = _[0].get("geometry")
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_pickle("save/police_pos.pickle")
        print(pd.read_pickle("save/police_pos.pickle"))

    def save_cctv_pos(self):
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]:"구별"}, inplace=True)
        pop.rename(columns={
            pop.columns[0] : "구별",
            pop.columns[1]: "인구수",
            pop.columns[2]: "한국인",
            pop.columns[3]: "외국인",
            pop.columns[4]: "고령자",
        }, inplace=True)
        pop.dropna(inplace=True)
        # print("*"*100)
        # print(pop)
        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        # print(cctv)
        cctv.drop(["2013년도 이전", "2014년", "2015년", "2016년"], axis=1, inplace=True)
        # print(cctv)
        cctv_pop = pd.merge(cctv, pop, on="구별")
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        # print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
        #       f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """
        cctv_pop.to_pickle("save/cctv_pos.pickle")
        print(pd.read_pickle("save/cctv_pos.pickle"))

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
    Crime().save_cctv_pos()