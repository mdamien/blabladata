import urldb
import json
from pprint import pprint as pp
from bs4 import BeautifulSoup

links = sorted(set(x['link'] for x in json.load(open('data/pages.json'))))

print(len(links),'links')

ALL = []

for link in links:
    print(link)
    infos = {'url':link}
    html = urldb.get(link)
    if html == None: continue
    e = BeautifulSoup(html,'lxml')
    all = e.find_all('meta')
    for el in all:
        if 'property' in el.attrs and 'blabla' in el.attrs['property']:
            content = el.attrs['content'].strip()
            attr_name = el.attrs['property'].split(':',1)[1].replace(':','_')
            infos[attr_name] = content
    #pp(infos)
    ALL.append(infos)
    json.dump(ALL, open('data/details.json','w'), indent=2)
    print(len(ALL))