import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split


'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB

'''

STROKE_MENUS = ["Exit", #0
                "spec",#1
                "Rename",#2
                "Interval",#3
                "Norminal",#4
                "Target",#5
                "Partition",#6
                "학습",#7
                "예측"]#8

stroke_meta = {
    'id' : '아이디',
    'gender' : '성별',
    'age' : '나이',
    'hypertension' : '고혈압',
    'heart_disease' : '심장병',
    'ever_married' : '기혼여부',
    'work_type' : '직종',
    'Residence_type' : '거주형태',
    'avg_glucose_level' : '평균혈당',
    'bmi' : '비만도',
    'smoking_status' : '흡연여부',
    'stroke' : '뇌졸중'
}

stroke_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.categorical_variables(),
    "5" : lambda t: t.partition(),
    "6" : lambda t: print(" ** No Function ** "),
    "7" : lambda t: print(" ** No Function ** "),
    "8" : lambda t: print(" ** No Function ** "),
}



class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
        self.adult_stock = None
    '''
    1.스펙보기
    '''
    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))

    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        # print(" --- 2.Features ---")
        # print(self.my_stroke.columns)

    '''
    3. 타겟변수(=종속변수 dependant, y값) 설정
    입력변수(=설명변수, 확률변수, x값)
    타깃변수명: stroke (=뇌졸중)
    타깃 변수값: 과거에 한 번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''

    def target(self):
        self.rename_meta()
        df = self.my_stroke

        print(f"id변수 데이터타입: {df['아이디'].dtypes}")
        print(f"id변수 결측값 개수: {df['아이디'].isnull().sum()}")
        print(f"id변수 유니크값 개수: {len(pd.unique(df['아이디']))}\n")

        print(f"타깃변수 데이터타입: {df['뇌졸중'].dtypes}")
        print(f"타깃변수 결측값 개수: {df['뇌졸중'].isnull().sum()}")
        print(f"타깃변수 데이터값 분포:\n{df['뇌졸중'].value_counts(dropna=False)}")
        print(f"타깃변수 데이터값 백분율:\n{df['뇌졸중'].value_counts(dropna=False, normalize=True)}\n")

    def interval_variables(self):
        self.rename_meta()
        df = self.my_stroke

        cols = ['나이', '평균혈당', '비만도']
        print(f"---구간변수타입---\n {df[cols].dtypes}")
        print(f"---결측값 있는 변수---\n {df[cols].isna().any()[lambda x: x]}")
        print(f"체질량 결측비율: {df['비만도'].isnull().mean():.2f}")

        pd.options.display.float_format = '{:.2f}'.format
        print(f"---구간변수 기초 통계량---\n{df[cols].describe()}")

        c = df['나이'] > 18
        self.adult_stock = df[c]
        print(f"---성인객체스펙---\n{df[c].shape}")

        c1 = self.adult_stock['평균혈당'] <= 232.64
        c2 = self.adult_stock['비만도'] <= 60.3
        self.adult_stock = self.adult_stock[c1 & c2]
        print(f'--- 이상치 제거한 성인객체스펙 ---\n{self.adult_stoke.shape}')

    def create_adult_stock(self):
        self.rename_meta()
        df = self.my_stroke
        c = df['나이'] > 18
        self.adult_stock = df[c]
        c1 = self.adult_stock['평균혈당'] <= 232.64
        c2 = self.adult_stock['비만도'] <= 60.3
        self.adult_stock = self.adult_stock[c1 & c2]

    def nominal_variables(self):
        self.create_adult_stock()
        df = self.adult_stock
        category = ['성별', '심장병', '기혼여부', '직종', '거주형태', '흡연여부', '고혈압']
        # print(f'범주형변수 데이터타입\n {df[category].dtypes}')
        # print(f'범주형변수 결측값\n {df[category].isnull().sum()}')
        # print(f'결측값 있는 변수\n {df[category].isna().any()[lambda x: x]}')
        # => 결측값이 없음.
        self.stroke = df
        self.spec()
        print(" ### 프리프로세스 종료 ### ")
        self.stroke.to_csv("./save/stroke.csv")

    def ordinal_variables(self):
        pass

    def partition(self):
        df = pd.read_csv('./save/stroke.csv')
        data = df.drop(['뇌졸중'], axis=1)
        target = df['뇌졸중']
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state=2)
        data_under, target_under = undersample.fit_resample(data, target)
        # print(target_under.value_counts(dropna=True))
        # print(target_under.value_counts(dropna=True, normalize=True))

        x_train, x_test, y_train, y_test = train_test_split(data_under, target_under, test_size=0.5, random_state=42, stratify=target_under)

        print("x_train shape:", x_train.shape)
        print("x_test shape:", x_test.shape)
        print("y_train shape:", y_train.shape)
        print("y_test shape:", y_test.shape)





