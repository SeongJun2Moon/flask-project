# from scp.domains import MelonMusic
from src.cop.scp.service.services import BugsMusic, MelonMusic


class ScrapController(object):

    @staticmethod
    def menu_0():
        print("끗")

    @staticmethod
    def menu_1(arg):
        print("벅스")
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        print("멜론")
        MelonMusic(arg)