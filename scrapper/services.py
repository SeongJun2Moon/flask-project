from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapper import MusicRanking


class BugsMusic(): # 함수형이 아닌 객체지향형으로 만든 건 db에 저장하겠다는 뜻
    arg = MusicRanking
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), "lxml")
    title = {"class" : arg.class_names[0]}
    artist = {"class" : arg.class_names[1]}
    titles = soup.find_all(name="p", attrs=title)
    artists = soup.find_all(name="p", attrs=artist)
    # 디버깅
    [print(f"{i+1} {titles[i].find('a').text} {j.find('a').text}\n") for i,j in zip(range(len(titles)),artists)]
    # dict 변환
    diction = {}
    for i,j in zip(titles, artists):
        diction[j.find('a').text] = i.find('a').text
    arg.diction = diction

    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.df_to_csv()