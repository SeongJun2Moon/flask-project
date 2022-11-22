import pandas as pd
from src.cmm.service.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        a = self.new_model('train.csv')
        return f"데이터의 타입: {type(a)}"

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = 'C:/Users/MSJ/AIA/flask-project/static/data/dam/bicycle/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df

    def create_bike(self):
        pass

    def create_label(self):
        pass