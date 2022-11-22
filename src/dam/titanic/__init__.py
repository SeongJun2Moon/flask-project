from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from src.cmm.service.common import Common
from src.dam.titanic.template import Plot
from src.dam.titanic.views import TitanicController

if __name__ == '__main__':
    api = TitanicController()
    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_sex()
            plot.draw_pclass()
            plot.draw_embarked()
        elif menu == "2":
            print(" ### 모델링 ### ")
            df = api.modeling('train.csv', 'test.csv')
        elif menu == "3":
            print(" ### 머신러닝 ### ")
            api.learning('train.csv', 'test.csv', [RandomForestClassifier(),
                                                   DecisionTreeClassifier(),
                                                   LogisticRegression()])
            # 랜덤 포레스트 분류기 83.05%
            # 결정트리분류기: 81.82 %
            # 로지스틱회귀: 77.89 %
            # 서포트벡터머신: ? %

        elif menu == "4":
            print(" ### 배포 ### ")
            df = api.submit('train.csv', 'test.csv')
        else:
            print(" ### 해당 메뉴 없음 ### ")