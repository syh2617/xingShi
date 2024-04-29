import bs4
import requests
import time
import re
import csv
from bs4 import BeautifulSoup

#存储所有  姓氏链接
def getLink():
    r = requests.get('https://www.xingmingzhijia.com/xingshi/')
    soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
    dll = soup.find('dl')
    k=[]
    z0 = 'https://www.xingmingzhijia.com'
    for aa in dll.find_all('a'):
        text = aa['href']
        full_link = f"https://www.xingmingzhijia.com{text}"
        k.append(full_link)
    return k

#爬取 每个姓氏url的html
def getHtml(url):
    try:
        rr=requests.get(url,timeout=30)
        rr.raise_for_status()
        rr.encoding='utf-8'
        return rr.text
    except Exception as ex:
        print("爬取{}网页时出错，出错原因：{}。".format(url,ex))
        return ""

#从每个姓氏html中，找出有用信息
def getTxt(html):
    soup2=bs4.BeautifulSoup(html, 'html.parser')

    chinese_text = ''
    for paragraph in soup2.find_all('p'):
        chinese_text += paragraph.get_text()
        chinese_text +='\n'
    lenn=len(chinese_text)
    txt=chinese_text[0:lenn-33]  #减去33 是为了 去掉字符串最后面的   “Copyright © 2020-2022 姓名之家 版权所有”
    return txt

#主程序
#先爬取特定姓氏链接，再进特定网站 爬取网站内容

xingshi=getLink() #存储所有姓氏链接

xing=[]#存储所有姓氏（起源、分布）的文字资料

i=0
for url in xingshi:#姓氏资料，循环爬

    html=getHtml(url)
    url2=url[36:]
    uuu=len(url2)
    han=url2[0:uuu-5]#姓氏 汉字

    txt=getTxt(html)
    xing.append(txt)
    time.sleep(1)

    with open("E:\\random\\csvFile.csv", 'a+', encoding='utf-8-sig',newline='') as csvFile:
        writer=csv.writer(csvFile)
        writer.writerow([han,txt])

    i=i+1
    print("{}{}finish {}.".format(i,han,url))
    #break


