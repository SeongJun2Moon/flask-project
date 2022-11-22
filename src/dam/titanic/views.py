from src.cmm.service.dataset import Dataset
from src.dam.titanic.models import TitanicModel


class TitanicController(object):


    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()


    def preprocess(self, train, test) -> object: # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정
        # this = model.pclass_ordinal(this) 데이터자체가 이미 오디널이다.
        this = model.sex_norminal(this) # 프로토 타입
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_norminal(this)
        this = model.title_norminal(this)
        this = model.drop_features(this, 'PassengerId','Name', 'Sex', 'Age', 'SibSp',
                                   'Parch', 'Ticket', 'Fare', 'Cabin')

        return this

    def modeling(self, train, test) -> object: # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self, train, test, algo): # 머신러닝
        model = self.model
        this = self.modeling(train, test)
        accuracy = model.get_accuracy(this, algo[0])
        accuracy2 = model.get_accuracy(this, algo[1])
        accuracy3 = model.get_accuracy(this, algo[2])
        print(f"랜덤포레스트 분류기 : {accuracy}%\n"
              f"결정트리분류기: {accuracy2} %\n"
              f"로지스틱회귀: {accuracy3}")

    def submit(self): # 배포
        pass

if __name__=="__main__":
    t = TitanicController()
    this = Dataset()
    this = t.modeling('train.csv', 'test.csv')
    print(this.train.head())
    print(this.train.columns)