# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/zashii/Library/Python/3.8/lib/python/site-packages')
import requests
from bs4 import BeautifulSoup

rq = requests.get('https://www.yahoo.co.jp')
print(rq.text)

list(range(3,6))

list_a =['dog','cat','tiger','horse','monkey']
for s in li[:]:
    if len(s)== 5:
        list_a.append(s)

list_a