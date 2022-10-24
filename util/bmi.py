'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''

class Bmi(object):
    def __init__(self, name, cm, kg) -> None:
        self.name = name
        self.cm = cm
        self.kg = kg

    def print(self):
        biman = self.kg/(self.cm**2)*10000
        if biman >= 35:
            bmi = "고도비만"
        elif biman <= 34.9 and biman >= 30:
            bmi = "중(重)도 비만 (2단계 비만)"
        elif biman <= 29.9 and biman >= 25:
            bmi = "경도 비만 (1단계 비만)"
        elif biman <= 24.9 and biman >= 23:
            bmi = "과체중"
        elif biman <= 22.9 and biman >= 18.5:
            bmi = "정상"
        else: bmi = "저체중"
        print(f"***************************\n이름 키(cm) 몸무게(kg) 비만도\n***************************")
        print(f"{self.name} {self.cm} {self.kg} {bmi}")
        print("***************************")

    @staticmethod
    def main():
        name = input("이름: ")
        cm = int(input("키: "))
        kg = int(input("몸무게: "))
        bmi = Bmi(name, cm, kg)
        bmi.print()

Bmi.main()