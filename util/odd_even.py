from random_list import RandomList

class OddEven(object):

    def __init__(self)->None:
        pass

    def __str__(self):
        rn = RandomList
        rl = rn.get_random(1,101,10)

        for i in range(len(rl)):
            [rl[j], rl[j + 1] = rl[j + 1], rl[j]
            for j in range(len(rl - 1) if rl[j] > rl[j + 1])]
            # for j in range(len(rl-1)):
            #     if rl[j] > rl[j+1]:
            #         rl[j], rl[j+1] = rl[j+1], rl[j]
        return rl
    @staticmethod

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu("랜덤숫자")
            if menu == 1:
                ls.append(OddEven.new_number())
            elif menu == 2:
                OddEven.print_numbers(ls)
            elif menu == 3:
                OddEven.delete_number(ls, input("삭제할 숫자: "))
            elif menu == 4:
                print("종료")
                break
            else: print("그런거 없음")

OddEven.main()

OddEven.main()