class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def menu(ls):
        [print(f"{i}:{j}") for i, j in enumerate(ls)]
        return input("메뉴 선택: ")

