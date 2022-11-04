from matplotlib import pyplot as plt
from PIL import Image
import cv2 as cv
import numpy as np

from canny.models import Executelambda, Hough, Harr
import requests
from io import BytesIO
from const.crawler import HEADERS
from util.dataset import Dataset


class MenuController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = Executelambda("IMAGE_READ-CV", params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Gray', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        img = Executelambda("URL", params[1])
        gray = Executelambda("gray_scale", img)
        plt.imshow(Executelambda("IMAGE_FROM_ARRAY", gray))
        plt.show()

    @staticmethod
    def menu_3(*params):
        img = Executelambda("URL", params[1])
        edges = cv.Canny(img, 100, 200)
        print(f"image type: {type(img)}")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        img = Executelambda("URL", params[1])
        edges = cv.Canny(img, 100, 200)
        dst = Hough(edges)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):

        # 오리지널 사진
        dt = Dataset()
        girl = Executelambda("IMAGE_READ-PLT", params[2])
        plt.subplot(151), plt.imshow(Image.fromarray(girl))
        plt.title('Original'), plt.xticks([]), plt.yticks([])

        # 회색 사진
        girl_gray = Executelambda("gray_scale", girl)
        plt.subplot(152), plt.imshow(Image.fromarray(girl_gray))
        plt.title('Gray'), plt.xticks([]), plt.yticks([])

        # 엣지 사진
        edges = cv.Canny(girl, 10, 100)
        plt.subplot(153), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])

        # 라인 사진
        dst = Hough(edges)
        plt.subplot(154), plt.imshow(dst, cmap='gray')
        plt.title('Line'), plt.xticks([]), plt.yticks([])

        # 하르 사진
        Harr(dt, girl, params)
        plt.subplot(155), plt.imshow(girl, cmap='gray')
        plt.title('Harr'), plt.xticks([]), plt.yticks([])

        plt.show()



    @staticmethod
    def menu_6(*params):
        pass