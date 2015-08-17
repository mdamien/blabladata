import urldb
import json
from pprint import pprint as pp
from bs4 import BeautifulSoup
import itertools

BASE_URL = "https://www.blablacar.co.uk"
URL = BASE_URL+"/search_xhr?fn=Paris&fc=48.856614%7C2.352222&fcc=FR&tn=&sort=trip_date&order=asc&limit=100&page={page}&_=1439842190324"

ALL = []

i = 0
while True:
    i += 1
    resp = urldb.get(URL.format(page=i))
    html = json.loads(resp)['html']['results']
    soup = BeautifulSoup(html,'lxml')
    elements = soup.find_all(class_='trip')
    for e in elements:
        infos = {}
        infos['link'] = BASE_URL+e.find('a').attrs['href']
        pp(infos)
        ALL.append(infos)

    print(len(elements))

    json.dump(ALL, open('data/pages.json','w'), indent=2)

    if len(elements) < 10:
        break

    print(len(ALL))
