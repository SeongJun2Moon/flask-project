import numpy as np
import pandas as pd
from util.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass칸등급', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare티켓가격', 'Cabin', 'Embarked정착부두']
시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
Pclass 
Sex 
Age 
Fare 
Embarked 
 === null 값 ===
 Age            177
 Cabin          687
 Embarked         2
"""
class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass
    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f'Train type: {type(b)}\n' \
               f'Train columns: {b.columns}\n' \
               f'Train head : {b.head()}\n' \
               f'Train null의 갯수 : {b.isnull().sum()}'
    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this):
        return this.train["Survived"]

    @staticmethod
    def drop_features(this, *feature) -> object: # feature 몇 개인지 모르지만
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    # @staticmethod
    # def pclass_ordinal(this) -> object: # 1,2,3등칸
    #     train = this.train
    #     test = this.test
    #     print(train['Pclass'])
    #     return this

    @staticmethod
    def sex_norminal(this) -> object: # male,female
        for i in [this.train, this.test]:
            i["Gender"] = i["Sex"].map({"male" : 0, "femail" : 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object: # 10대 20대 30대
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5) # 0.5나이는 없음 = 연령미상 -1 ~ 0(unknown)을 의미함
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf] # 68세 이상은 무한대로 취급
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object: # 비싸, 보통, 싸
        for i in [this.train, this.test]:
            i["Fareband"] = pd.qcut(i['Fare'], q = 4, labels = [1, 2, 3, 4])
        return this

    @staticmethod
    def embarked_nominal(this) -> object: # 승선항구 s,c,q
        this.train = this.train.fillna({"Embarked" : "S"})
        this.test = this.test.fillna({"Embarked": "S"})
        for i in [this.train, this.test]:
            i["Embarked"] = i["Embarked"].map({"S" : 1, "C" : 2, "Q" : 3})
        return this

if __name__ == '__main__': # 테스트용
    t = TitanicModel()
    this = t.dataset
    this.train = t.new_model('train.csv')
    this.test = t.new_model("test.csv")
    this = TitanicModel.age_ordinal(this)
    print(this.train.isnull().sum())
    # array = np.arange(4) # 튜플 만들기
    # array = np.random.randint(0,10,(3,3)) # 테이블 만들기