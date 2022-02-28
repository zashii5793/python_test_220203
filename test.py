# resuests モジュールをインポート
import requests

# Webサイトの情報を変数rに格納し、そのうちのテキスト部分を出力
r = requests.get("https://news.yahoo.co.jp/")
print(r.text)
