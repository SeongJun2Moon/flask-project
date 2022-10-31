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
        print(f"cv2 버전: {cv2.__version__}")
        img = cv2.imread(self.model.new_model(fname), cv2.IMREAD_COLOR)
        print(f'Shape is {img.shape}')
        cv2.imshow(self.model.new_model(fname), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def learning(self):
        pass

    def submit(self):
        pass