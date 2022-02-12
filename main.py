# -*- coding: utf-8 -*-
from http.client import GONE, OK
import sys
from xml.dom import SyntaxErr
sys.path.append('/Users/zashii/Library/Python/3.8/lib/python/site-packages')
import requests
from bs4 import BeautifulSoup

code = 9020 #JR東日本の証券コード

#指定URLのHTMLデータを取得
url = "https://minkabu.jp/stock/{0:d}/settlement".format(code)
html = requests.get(url)

# BeautifulSoupのHTMLパーサーを生成
soup = BeautifulSoup(html.content, "html.parser")

# 全<table>要素を抽出
table_all = soup.find_all('table')

# 決算情報の<table>要素を検索する。
fin_table1 = None
for table in table_all:
    
    # <caption>要素を取得
    caption = table.find('caption')
    if caption is None:
        continue
    
    # <caption>要素の文字列が目的のものと一致したら終了
    if caption.text == '決算情報':
        fin_table1 = table
        break

# <table>要素内のヘッダ情報を取得する。
headers = []
thead_th = fin_table1.find('thead').find_all('th')
for th in thead_th:
    headers.append(th.text)

# <table>要素内のデータを取得する。
rows = []
tbody_tr = fin_table1.find('tbody').find_all('tr')
for tr in tbody_tr:
    
    # 1行内のデータを格納するためのリスト
    row = []
    
    # <tr>要素内の<th>要素を取得する。
    th = tr.find('th')
    row.append(th.text)
    
    # <tr>要素内の<td>要素を取得する。
    td_all = tr.find_all('td')
    for td in td_all:
        row.append(td.text)
    
    # 1行のデータを格納したリストを、リストに格納
    rows.append(row)


# DataFrameを生成する
df = pd.DataFrame(rows, columns=headers)

# 先頭の列(決算期)をインデックスに指定する
df = df.set_index(headers[0])

def trim_camma(x):
    # 2,946,639.3のようなカンマ区切り、小数点有りの数値か否か確認する
    comma_re = re.search(r"(\d{1,3}(,\d{3})*(\.\d+){0,1})", x)
    if comma_re:
        value = comma_re.group(1)
        value = value.replace(',', '') # カンマを削除
        return np.float64(value) # 数値に変換
    
    return x

# 各列に対して、trim_cammaを適用する
new_df = df.copy()
for col in df.columns:
    new_df[col] = df[col].map(lambda v : trim_camma(v))

# 括弧内の文字列を削除する関数(括弧自体も削除する)
def remove_inparentheses(s):
    
    # 文字列末尾の括弧を削除する
    result = re.search(r"(.+)(\(.+\))", s)
    if result:
        str = result.group(1)
        return str
    
    return s

# インデックス(決算情報)の括弧内要素を削除する。
new_df.index.name = remove_inparentheses(new_df.index.name)
new_df.index = new_df.index.map(lambda s : remove_inparentheses(s))
