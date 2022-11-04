from titanic.models import TitanicModel
from util.dataset import Dataset

class TitanicController(object):
    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()

    def mining(self):
        pass
    def preprocess(self, train, test) -> object:  # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정
        # this = model.pclass_ordinal(this) # 수정없이 순서만 정하면 됨
        this = model.sex_norminal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this) # 내부 스칼라의 props가 바귐
        this = model.title_norminal(this)
        this = model.drop_features(this, "PassengerId", "Name", "Sex", "Age",
                                   "SibSp", "Parch", "Ticket", "Fare", "Cabin")
        return this

    def modeling(self, train, test) -> object:  # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this) # 답안지
        this.train = model.create_train(this)
        return this

    def learning(self):  # 기계학습
        pass

    def submit(self):  # 배포
        pass

if __name__ == '__main__':
    tc = TitanicController()
    this = tc.modeling('train.csv',"test.csv")
    print(this.train.head(6))
    print(this.train.columns)
    print(this.train.isnull)
