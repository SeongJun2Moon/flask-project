import urllib.request
from urllib.request import urlopen


from bs4 import BeautifulSoup


def BugsMusic(arg): # 함수형이 아닌 객체지향형으로 만든 건 db에 저장하겠다는 뜻
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), "lxml")
    title = {"class" : arg.class_names[0]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artist = {"class": arg.class_names[1]}
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]

    # 디버깅
    [print(f"{i+1}위 {titles[i]} : {j}") for i, j in zip(range(len(titles)), artists)]

    # dict 로 변환
    diction = {}
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction

    # csv파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()
def MelonMusic(arg):
    soup = BeautifulSoup(urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent' : "Mozilla/5.0"})), "lxml")
    title = {"class": arg.class_names[0]}
    titles = soup.find_all(name=arg.tagname, attrs=title)
    titles = [i.find('a').text for i in titles]
    artist = {"class": arg.class_names[1]}
    artists = soup.find_all(name=arg.tagname, attrs=artist)
    artists = [i.find('a').text for i in artists]

    # 디버깅
    [print(f"{i+1}위 {titles[i]} : {j}") for i, j in zip(range(len(titles)), artists)]
    #
    # # dict 로 변환
    # diction = {}
    # for i, j in enumerate(titles):
    #     diction[j] = artists[i]
    # arg.diction = diction
    #
    # # csv파일로 저장
    # arg.dict_to_dataframe()
    # arg.dataframe_to_csv()