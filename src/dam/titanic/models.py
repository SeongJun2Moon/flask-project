import numpy as np
import pandas as pd


from sklearn.model_selection import KFold # 머신러닝 라이브러리
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # 랜덤 포레스트 분류기

from src.cmm.service.dataset import Dataset

"""
 ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
 시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
 === 상관 관계 ===
 Pclass 
 Sex
 Age
 Fare
 Embarked
 === null 값 === null 값 있을땐 for 문 돌리면 에러걸림
 Age      177
 Cabin     687
 Embarked  2
 """


class TitanicModel(object):

    dataset = Dataset()
    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f" Train type : {type(b)} \n" \
               f"Train columns : {b.columns} \n" \
               f"Train head : {b.head()}\n" \
               f"Train null의 갯수 : {b.isnull().sum()}"

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = '../../../static/data/dam/titanic/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # drop은 dataset 에 있는 train에 있는 Suvived열을 지운다
    @staticmethod
    def create_label(this) -> object: # test용은 label
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object: # *feature 에잇는 *은 지료구조라는 표시임
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this
    """
    @staticmethod
    def pclass_ordinal(this) -> object: # 1, 2, 3등칸
        train = this.train
        test = this.test
        return this
    """
    @staticmethod
    def sex_norminal(this) -> object: # female -> 1 , male -> 0
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male" : 0, "female" : 1}) # mapping 할때 쓰는게 dc임
        return this
    @staticmethod
    def age_ordinal(this) -> object: # 10대, 20대, 30대
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)     # -0.5는 확인 할 수 없으니 빼버린다는 의미
        bins = [-1, 0, 5, 12, 18, 24, 35, 68,np.inf]  # bins 는 값을 하나씩 할당 하겠다는 의미 np.inf는 max를 뛰어 넘으면~ 이런 식의 표현
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] =  i['AgeGroup'].map(age_mapping)
        return this
    @staticmethod
    def fare_ordinal(this) -> object: # 비싼거, 보통, 저렴한 것  4등분 pd.qcut()
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=[1, 2, 3, 4] )
        return this
    @staticmethod
    def embarked_norminal(this) -> object: # 승선항구 S, C, Q
        this.train = this.train.fillna({"Embarked":"S"})    # fillna 는 null 값을 임의로 넣으라는 뜻
        this.test = this.test.fillna({"Embarked": "S"})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C" : 2, "Q" : 3}) # 같은 이름을 넣으면 원래 이름에 덮어짐 train,test파일에 스칼라가 추가 되는 것이 아님.
        return this
    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)  # Name에 str값을 뽑아낸다. ([A-Za-z]+)\. 는 영어 전체를  expand 는 맞는거만 가져와라
        for i in combine:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')        # replace는  앞에 값을 뒤에 값으로 변환 한다 라는의미
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map({
                'Mr': 1,
                'Miss': 2,
                'Mrs': 3,
                'Master': 4,
                'Royal': 5,
                'Rare': 6
            })
        return this

    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10, shuffle=True, random_state=0) # KFold 객체
    @staticmethod
    def get_accuracy(this, algo):
        score = cross_val_score(algo,
                                this.train,
                                this.label,
                                cv=TitanicModel.create_k_fold() ,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score)*100,2)

if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.sex_norminal(this)
    this = TitanicModel.fare_ordinal(this)
    this = TitanicModel.embarked_norminal(this)
    this = TitanicModel.age_ordinal(this)
    print(this.train.columns)
    print(this.train.head())
    print(this.test.columns)