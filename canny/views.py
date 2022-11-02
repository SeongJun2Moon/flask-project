from matplotlib import pyplot as plt
from PIL import Image
import cv2 as cv
import numpy as np
from canny.models import image_read, GaussianBlur, Canny, gray_scale
import requests
from io import BytesIO
from const.crawler import HEADERS


class MenuController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = image_read(params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Gray', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        res = requests.get(params[1], headers=HEADERS)
        img = np.array(Image.open(BytesIO(res.content)))
        gray = gray_scale(img)
        gray = GaussianBlur(gray, 1, 1)
        # gray = Canny(gray, 50, 150)
        plt.imshow(Image.fromarray(gray))
        plt.show()

    @staticmethod
    def menu_3(*params):
        res = requests.get(params[1], headers=HEADERS)
        img = np.array(Image.open(BytesIO(res.content)))
        edges = cv.Canny(img, 100, 200)
        print(f"image type: {type(img)}")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        res = requests.get(params[1], headers=HEADERS)
        img = np.array(Image.open(BytesIO(res.content)))
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()


#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return f""
#
#     dataset = Dataset()
#
#     def preprocess(self, fname) -> object:  # 전처리
#         img = self.model.new_model(fname)
#         return img
#
#     def modeling(self, fname) -> object:
#         img = self.preprocess(fname)
#         return img
#
#     def CannyModeling(self, url):
#         CannyModel(url).get()
#
#     def learning(self):  # 기계학습
#         pass
#
#     def submit(self):  # 배포
#         pass
#
#
# if __name__ == "__main__":
#     pass