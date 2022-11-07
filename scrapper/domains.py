from dataclasses import dataclass

import urllib.request
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX

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
        arg = MusicRanking()
        soup = BeautifulSoup(urlopen(self.url), "lxml")
        title = {"class" : arg.class_names[0]}
        artist = {"class" : arg.class_names[1]}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        # 디버깅
        [print(f"{i+1} {titles[i].find('a').text} {j.find('a').text}\n") for i,j in zip(range(len(titles)),artists)]
        # dict 파일로 변환
        for i in range(0, len(titles)):
            arg.dic[arg.titles[i]] = arg.artists[i]

        # csv 파일로 저장
        arg.dict_to_dataframe()
        arg.df_to_csv()

class MelonMusic:

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent' : "Mozilla/5.0"}

    def scrap(self):
        soup = BeautifulSoup(urlopen(urllib.request.Request(self.url, headers=self.headers)), "lxml")
        titles = soup.find_all(name="div", attrs={"class" : "rank01"})
        artists = soup.find_all(name="div", attrs={"class" : "rank02"})
        [print(f"{i+1} {titles[i].find('a').text} {j.find('a').text}\n") for i,j in zip(range(len(titles)),artists)]

@dataclass
class MusicRanking:
    html : str
    parser : str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname : str
    class_names : []
    artists : []
    titles : []
    diction : {}
    df : None
    soup : BeautifulSoup

    @property
    def html(self): return self._html
    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self): return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def soup(self): return self._soup
    @soup.setter
    def soup(self, soup): self._soup = soup

    @property
    def domain(self): return self._domain
    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self): return self._query_string
    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self): return self._headers
    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self): return self._tag_name
    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self): return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self): return self._class_names
    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self): return self._artists
    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self): return self._titles
    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def diction(self): return self._diction
    @diction.setter
    def diction(self, diction): self._diction = diction

    @property
    def df(self): return self._df
    @df.setter
    def df(self, df): self._df = df

    def dict_to_dataframe(self):
        print("^" * 10)
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')
        print("*"*10)
        print(self.df)

    def dataframe_to_csv(self):
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN")