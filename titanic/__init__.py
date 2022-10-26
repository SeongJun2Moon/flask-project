from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    api = TitanicController()
    while True:
        menu = Common.menu(["종류", "시각화", "모델링", "머신 러닝", "베포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_sex()
            # plot.draw_pclass()
            # plot.draw_survived()
        elif menu == "2":
            print(" ### 모델링 ### ")
        elif menu == "3":
            print(" ### 머신 러닝 ### ")
        else : print("그런거 없음")