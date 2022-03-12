# resuests モジュールをインポート
import requests
from bs4 import BeautifulSoup

# Webサイトの情報を変数rに格納し、そのうちのテキスト部分を出力
r = requests.get("https://news.yahoo.co.jp/")
soup = BeautifulSoup(r, "html.parser")
print(r)

