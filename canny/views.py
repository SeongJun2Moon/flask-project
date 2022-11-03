from matplotlib import pyplot as plt
from PIL import Image
import cv2 as cv
import numpy as np

from canny.models import image_read, gray_scale, Executelambda
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
        img = Executelambda("IMAGE_READ", params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Gray', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        res = requests.get(params[1], headers=HEADERS)
        img = np.array(Image.open(BytesIO(res.content)))
        gray = Executelambda("gray_scale", img)
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
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):

        # 오리지널 사진
        dt = Dataset()
        girl = params[2]
        girl = image_read(girl)
        plt.subplot(151), plt.imshow(Image.fromarray(girl))
        plt.title('Original'), plt.xticks([]), plt.yticks([])

        # 회색 사진
        girl_gray = gray_scale(girl)
        plt.subplot(152), plt.imshow(Image.fromarray(girl_gray))
        plt.title('Gray'), plt.xticks([]), plt.yticks([])

        # 엣지 사진
        edges = cv.Canny(girl, 10, 100)
        plt.subplot(153), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])

        # 라인 사진
        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 10, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(154), plt.imshow(dst, cmap='gray')
        plt.title('Line'), plt.xticks([]), plt.yticks([])

        # 하르 사진
        haar = cv.CascadeClassifier(dt.context+params[1])
        face = haar.detectMultiScale(girl, minSize=(150, 150))
        if len(face) == 0:
            print("얼굴인식 실패")
            quit()
        for(x,y,w,h) in face:
            print(f"얼굴 좌표 : {x},{y},{w},{h}")
            red = (255,0,0)
            cv.rectangle(girl, (x,y), (x+w, y+h), red, thickness=10)
        plt.subplot(155), plt.imshow(girl, cmap='gray')
        plt.title('Harr'), plt.xticks([]), plt.yticks([])

        plt.show()

    @staticmethod
    def menu_6(*params):
        pass