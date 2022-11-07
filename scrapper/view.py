from scrapper.domains import BugsMusic, MelonMusic


class MenuController(object):

    @staticmethod
    def menu_0():
        print("끗")

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        melon = MelonMusic(arg)
        melon.scrap()