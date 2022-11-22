from src.cmm.service.common import Common
from src.dam.bicycle.models import BicycleModel
from src.dam.bicycle.views import BicycleController



api = BicycleController()
while True:
    menu = Common.menu(["종류", "시각화", "모델링", "머신 러닝", "베포"])
    if menu == "0":
        print(" ### 종료 ### ")
        break
    elif menu == "1":
        print(" 터미널 출력 ")
        print(BicycleModel())
        # a = BicycleModel().new_model('train.csv')
        # print(f"데이터의 타입: {type(a)}")
        # print(f"데이터의 columns: \n{a.columns}")
        # print(f"데이터의 head: \n{a.head()}")
        # print(f"데이터의 null 개수 = \n{a.isnull().sum()}")
    elif menu == "2":
        print(" ### 모델링 ### ")
    elif menu == "3":
        print(" ### 머신 러닝 ### ")
    else : print("그런거 없음")