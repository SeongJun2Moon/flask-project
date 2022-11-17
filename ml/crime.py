import googlemaps
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pickle
import folium


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CRIME_MENUS = ["Exit", #0
            "Spec",#1
            "save_police_pos",#2
            "save_cctv_pos",#3
            "save_police_norm",#4
            "Ordinal",#5
            "Partition"]#6

crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pos(),
    "4" : lambda t: t.save_police_norm,
    "5" : lambda t: t.interval(),
    "6" : lambda t: t.ratio(),
    "7" : lambda t: t.partition()
}



class Crime:

    def __init__(self):
        self.crime = pd.read_csv("data/crime_in_seoul.csv")
        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)

        self.cctv = pd.read_csv("data/cctv_in_seoul.csv")
        self.pop = pd.read_excel("data/pop_in_seoul.xls", skiprows=[0, 2])[["자치구", "합계", "한국인", "등록외국인", "65세이상고령자"]]
        self.ls = [self.crime, self.cctv, self.pop]

        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']

    '''
    1.스펙보기 
    id = SERIALNO  
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
      '절도 검거', '폭력 발생', '폭력 검거'],
     dtype='object')
    Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object'
    '''
    def spec(self):
        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                          f"--- 2.Features ---\n{x.columns}\n"
                          f"--- 3.Info ---\n{x.info}\n"
                          f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                          f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                          f"--- 6.Describe ---\n{x.describe()}\n"
                          f"--- 7.Describe All ---\n{x.describe(include='all')}"))(i)
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
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'
        crime.to_pickle("save/police_pos.pkl")
        print(pd.read_pickle("save/police_pos.pkl"))


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
        cctv_pop.to_pickle("save/cctv_pos.pkl")
        print(pd.read_pickle("save/cctv_pos.pkl"))

    def save_police_norm(self):
        police_pos = pd.read_pickle("save/police_pos.pkl")
        # print(police_pos.head(10))
        # print("/" * 100)
        police = pd.pivot_table(police_pos, index="구별", aggfunc=np.sum)
        # print(police)
        police['살인검거율'] = police['살인 검거'].astype(int) / police['살인 발생'].astype(int) * 100
        police['강도검거율'] = police['강도 검거'].astype(int) / police['강도 발생'].astype(int) * 100
        police['강간검거율'] = police['강간 검거'].astype(int) / police['강간 발생'].astype(int) * 100
        police['절도검거율'] = police['절도 검거'].astype(int) / police['절도 발생'].astype(int) * 100
        police['폭력검거율'] = police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int) * 100
        police.drop(columns={"살인 발생", "강도 발생", "강간 발생", "절도 발생", "폭력 발생"})

        for i in self.crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)

        x = police[self.crime_rate_columns].values
        min_max_scaler = preprocessing.MinMaxScaler()
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """

        x_scaled = min_max_scaler.fit_transform(x.astype(float)) # int타입을 float로 바꿈 = 연속형으로 변환

        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """

        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        print(police_norm)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        police_norm.to_pickle("save/police_norm.pkl")
        print(pd.read_pickle("save/police_norm.pkl"))

    def folium_example(self):
        pass

    def ordinal(self):
        pass

    def interval(self):
        pass

    def ratio(self):
        pass

    def partition(self):
        pass

if __name__ == '__main__':
    Crime().save_police_norm()