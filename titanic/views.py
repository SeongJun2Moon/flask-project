from titanic.models import TitanicModel
from util.dataset import Dataset
class TitanicController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self) -> object: # 전처리
        pass

    def modeling(self) -> object: # 모델생성
        self.preprocess()

    def learning(self): # 기계학습
        pass

    def submit(self): # 배포
        pass