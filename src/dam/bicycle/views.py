from src.cmm.service.dataset import Dataset
from src.dam.bicycle import BicycleModel


class BicycleController(object):

    dataset = Dataset()
    model = BicycleModel()

    def __init__(self):
        pass

    def __str__(self):
        return f"sadf"

    def mining(self):
        pass

    def preprocess(self, bike, test) -> object:
        model = self.model
        this = self.dataset
        this.bike = model.new_model(bike)
        this.test = model.new_model(test)
        this.id = this.test['id']
        # column 편집
        return this

    def modeling(self, bike, test):
        model = self.model
        this = self.preprocess(bike, test)
        this.label = model.create_label(this)
        this.bike = model.create_bike(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass