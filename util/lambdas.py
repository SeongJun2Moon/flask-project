from io import BytesIO
import numpy as np
import requests
from PIL import Image
from const.crawler import HEADERS
import cv2 as cv
from util.dataset import Dataset
from const.path import CTX

def MosaicLambda(*params):
    cmd = params[0]
    target = params[1]
    ds = Dataset()
    if cmd == "IMAGE_READ-CV":
        return (lambda x : cv.imread( + x))(target)
    elif cmd == "IMAGE_READ-PLT":
        return (lambda x : cv.cvtColor(cv.imread(CTX + x), cv.COLOR_BGR2RGB))(target)
    elif cmd == "gray_scale":
        return (lambda x : x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(target)
    elif cmd == "URL":
        res = requests.get(params[1], headers=HEADERS)
        img = np.array(Image.open(BytesIO(res.content)))
        return img
    elif cmd == "IMAGE_FROM_ARRAY":
        return (lambda x : Image.fromarray(x))(target)