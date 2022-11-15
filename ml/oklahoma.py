import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


okl_MENUS = ["종료", #0
                "데이터구조파악",#1
                "변수한글화",#2
                "연속형변수편집",#3
                "범주형변수편집",#4
                "샘플링",#5
                "학습",#6
                "예측"]#7

oklahoma_meta = {
    'ACCESS' : 'ACCESS',
    'ACR' : 'ACR',
    'AGEP' : '나이',
    'BATH' : 'BATH',
    'BDSP' : '침실수',
    'BLD' : 'BLD',
    'CONP' : 'CONP',
    'COW' : 'COW',
    'ELEP' : '월전기료',
    'FESRP' : 'FESRP',
    'FKITP' : 'FKITP',
    'FPARC' : 'FPARC',
    'FSCHP' : 'FSCHP',
    'FTAXP' : 'FTAXP',
    'GASP' : '월가스비',
    'HHL' : 'HHL',
    'HHT' : 'HHT',
    'HINCP' : '가계소득',
    'ANX' : 'ANX',
    'MAR' : 'MAR',
    'MV' : 'MV',
    'NRC' : '자녀수',
    'R18' : 'R18',
    'R65' : 'R65',
    'RAC1P' : 'RAC1P',
    'RMSP' : '방수',
    'RWAT' : 'RWAT',
    'SCH' : 'SCH',
    'SCHL' : 'SCHL',
    'SEX' : 'SEX',
    'VALP' : '주택가격',
    'VALP_B1' : '지하주택가격'
    }

okl_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.categorical_variables(),
    "5" : lambda t: t.sampling(),
    "6" : lambda t: print(" ** No Function ** "),
    "7" : lambda t: print(" ** No Function ** "),
    "8" : lambda t: print(" ** No Function ** "),
}

class Oklahoma:
    pd.options.display.float_format = '{:.3f}'.format

    def __init__(self):
        self.df = pd.read_csv("data/comb32.csv")
        self.non_valp_df = None


    def spec(self):
        df = self.df
        # print(" --- 1.Shape ---")
        # print(self.df.shape)
        # print(" --- 2.Features ---")
        # print(self.df.columns)
        # print(" --- 3.Info ---")
        # print(self.df.info())
        # print(" --- 4.Case Top1 ---")
        # print(self.df.head(1))
        # print(" --- 5.Case Bottom1 ---")

    def type_sep(self):
        print(self.df[['AGEP', 'BDSP', 'CONP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP']].dtypes)

    def interval_variables(self):
        df = self.df
        cols1 = ['AGEP', 'BDSP', 'CONP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP'] # 구간변수 처리 시작
        # print(df[cols1].describe())
        # print(df[cols1].skew())
        # print(df[cols1].kurtosis())
        # print(df['CONP'].value_counts(normalize=True))
        df.drop('CONP', axis=1, inplace=True) # 구간변수 필터링
        # print(df.shape)
        c1 = df['ELEP'] <= 500
        c2 = df['GASP'] <= 311
        c3 = df['HINCP'] <= 320000
        df = df[c1 & c2 & c3]
        cols2 = ['AGEP', 'BDSP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP'] # 필터링에서 'CONP' 빠짐
        # print(df[cols2].describe())
        # print(df['VALP_B1'].value_counts(normalize=True)) #com31

        # group= df['AGEP'].groupby(df['VALP_B1'])
        # print(group.mean())
        # group2 = df['ELEP'].groupby(df['VALP_B1'])
        # print(group2.mean())
        # group3 = df['GASP'].groupby(df['VALP_B1'])
        # print(group3.mean())
        # group4 = df['HINCP'].groupby(df['VALP_B1'])
        # print(group4.mean())

        # 귀무가설 판별

        # print(df.isna().any()[lambda x:x])

        self.non_valp_df = df.drop(['VALP'], axis=1)



    def norminal_variables(self):
        self.interval_variables()
        df = self.non_valp_df
        # print(df['MAR'].value_counts(dropna=False))  # 범주형 변수(=결혼여부)의 데이터분석
        self.non_valp_df = df

    def partition(self):
        self.norminal_variables()
        df = self.non_valp_df
        data = df.drop(["VALP_B1"], axis=1)
        target = df['VALP_B1']
        # print(data.shape)
        # print(target.shape)

        x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.5, random_state=42)
        print("x_train shape:", x_train.shape)
        print("x_test shape:", x_test.shape)
        print("y_train shape:", y_train.shape)
        print("y_test shape:", y_test.shape)

        df.to_csv("./save/oklahoma.csv")



if __name__ == '__main__':
    Oklahoma().partition()

