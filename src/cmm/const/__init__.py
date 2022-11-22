import googlemaps

if __name__ == '__main__':
    key = "AIzaSyBgVssF55ids-IGxgRA0jx4-s2_2GoFxF8"
    gmaps = googlemaps.Client(key=key)
    print(gmaps.geocode("서울특별시 종로구 율곡로 99", language="ko"))


