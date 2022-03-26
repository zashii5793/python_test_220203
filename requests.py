#coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.nikkei.com/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.span

print (title_tag)

