#coding: utf-8
import sys
import urllib
import urllib.request
from bs4 import BeautifulSoup
 
question_word = "周长胜"
url = "http://www.baidu.com/s?wd=" + urllib.parse.quote(question_word.encode('utf-8').decode(sys.stdin.encoding).encode('gbk'))
htmlpage = urllib.request.urlopen(url).read()
soup = BeautifulSoup(htmlpage,"html.parser",from_encoding='utf-8') 
print(soup)
print(len(soup.findAll("a", {"class": ""})))
for result_table in soup.findAll("a", {"class": ""}):
    a_click = result_table.find("a")
    print("-----标题----\n")
    print(result_table.renderContents())#标题
    print("----链接----\n")
    print(str(result_table.get("href")))#链接
    print()