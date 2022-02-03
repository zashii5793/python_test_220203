# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/zashii/Library/Python/3.8/lib/python/site-packages')
import requests
import urllib3
import charset_normalizer

#import cchardet
#from bs4 import BeautifulSoup

rq = requests.get('https://www.yahoo.co.jp')
print('a')


#参考情報

# https://blog.saladbowl.work/blog/2020/09/mac-python3-flask/

#今回の場合、古いバージョンの
#pipコマンドがハッシュテーブルに記憶されているので、
#下記コマンド「hash -r」で情報を消去しましょう。
