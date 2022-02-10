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

for i in range(0,16,4):
    print(i)

for i in range(0,16,4):
    print(i,end=",")    

a=[4,18,1,10,15,19]

for i in range(6):
    b=5+a[i]
    if b>=20:
        print("  skip")
        continue
    print(b,i,a[i])    

def janken(name, content='tyoki',kaisu=3):
    print(name,end=',')
    print(content,end=',')
    print(kaisu)

janken(name='太郎',content='par')
