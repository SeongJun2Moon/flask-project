import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""

class BugsMusic: # 함수형이 아닌 객체지향형으로 만든 건 db에 저장하겠다는 뜻

    def __init__(self, url):
        self.url = url

    def scrap(self): # 정석
        soup = BeautifulSoup(urlopen(self.url), "lxml")
        title = {"class" : "title"}
        artist = {"class" : "artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        [print(f"{i+1} {titles[i].find('a').text} {j.find('a').text}\n") for i,j in zip(range(len(titles)),artists)]


class MelonMusic:

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent' : "Mozilla/5.0"}

    def scrap(self):
        soup = BeautifulSoup(urlopen(urllib.request.Request(self.url, headers=self.headers)), "lxml")
        titles = soup.find_all(name="div", attrs={"class" : "rank01"})
        artists = soup.find_all(name="div", attrs={"class" : "rank02"})
        [print(f"{i+1} {titles[i].find('a').text} {j.find('a').text}\n") for i,j in zip(range(len(titles)),artists)]


