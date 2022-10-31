import numpy as np
import pandas as pd
from util.dataset import Dataset
import cv2


class LennaModel(object):

    dataset = Dataset

    def __init__(self):
        pass

    def __str__(self):
        pass
    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return f"{this.context}{this.fname}"
