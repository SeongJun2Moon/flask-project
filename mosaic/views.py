from matplotlib import pyplot as plt
from PIL import Image
import cv2 as cv
import numpy as np
import copy
from const.path import CTX
from mosaic.services import Hough, Haar, mosaic

from util.dataset import Dataset
from util.lambdas import MosaicLambda


class MenuController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = MosaicLambda("IMAGE_READ-CV", params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Gray', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        img = MosaicLambda("URL", params[1])
        gray = MosaicLambda("gray_scale", img)
        plt.imshow(MosaicLambda("IMAGE_FROM_ARRAY", gray))
        plt.show()

    @staticmethod
    def menu_3(*params):
        img = MosaicLambda("URL", params[1])
        edges = cv.Canny(img, 100, 200)
        print(f"image type: {type(img)}")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        img = MosaicLambda("URL", params[1])
        edges = cv.Canny(img, 100, 200)
        dst = Hough(edges)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def menu_5(*params):
        print(params[0])
        cat = cv.imread(f"{CTX}{params[1]}")
        mos = mosaic(cat, 100)
        cv.imwrite(f'{CTX}cat-mosaic.png', mos)
        cv.imshow('CAT MOSAIC', mos)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_6(*params):

        # 오리지널
        girl = MosaicLambda("IMAGE_READ-PLT", params[2])
        plt.subplot(231), plt.imshow(Image.fromarray(girl))
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        girl2 = copy.deepcopy(girl)  # 모자이크에서 쓸 애

        # 그레이
        girl_gray = MosaicLambda("gray_scale", girl)
        plt.subplot(232), plt.imshow(Image.fromarray(girl_gray))
        plt.title('Gray'), plt.xticks([]), plt.yticks([])

        # 케니
        girl_edges = cv.Canny(girl, 30, 31)
        plt.subplot(233), plt.imshow(girl_edges, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])

        # 허프
        girl_hough = Hough(girl_edges)
        plt.subplot(234), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])

        # 하르
        girl_haar = Haar(girl)
        plt.subplot(235), plt.imshow(girl_haar, cmap='gray')
        plt.title('Harr'), plt.xticks([]), plt.yticks([])

        # 모자이크
        girl_mosic = mosaic(girl2, 10)
        plt.subplot(236), plt.imshow(girl_mosic, cmap='gray')
        plt.title('Mosic'), plt.xticks([]), plt.yticks([])

        plt.show()

    @staticmethod
    def menu_7(*params):
        print(params[0])
        photo = MosaicLambda("IMAGE_READ-PLT", params[2])
        mos = mosaic(photo, 10)
        plt.imshow(Image.fromarray(mos))
        plt.show()


# if __name__ == '__main__':
#     print(MenuController.menu_5())