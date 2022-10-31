from util.dataset import Dataset
from lena.models import LennaModel
import cv2

class LennaController(object):

    dataset = Dataset()
    model = LennaModel()

    def __init__(self):
        pass

    def __str__(self):
        pass

    def mining(self):
        pass

    def preprocess(self):
        pass

    def modeling(self, fname) -> object:
        img = self.model.new_model(fname)
        return img

    def learning(self):
        pass

    def submit(self):
        pass