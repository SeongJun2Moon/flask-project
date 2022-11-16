import googlemaps
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split

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
    "3" : lambda t: t.norminal(),
    "4" : lambda t: t.interval(),
    "5" : lambda t: t.ratio(),
    "6" : lambda t: t.partition()
}

class Crime:

    def __init__(self):
        self.crime = pd.read_csv("data/crime_in_seoul.csv")
        self.cctv = pd.read_csv("data/cctv_in_seoul.csv")
        self.pop = pd.read_excel("data/pop_in_seoul.xls", skiprows=[0, 2])[["자치구", "합계", "한국인", "등록외국인", "65세이상고령자"]].head(5)
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
            print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f"서울시내 경찰서는 총 {len(station_names)} 이다")
        [print(f"{i}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode("서울종로경찰서", language='ko'))

        print("API에서 주소추출 시작")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language="ko")
            print(f'name:{i} = {_[0].get("formatted_address")}')
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
        crime.to_csv("save/police_pos.csv", index=False)


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