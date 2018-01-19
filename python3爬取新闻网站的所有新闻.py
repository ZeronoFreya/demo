#coding: utf-8

from urllib import request, parse
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


##dfs算法遍历全站###
def dfs(url):
    print(url)
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = request.Request(url=url, headers=headers)
        html = request.urlopen(req).read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        trs = soup.findAll('tr', 'bd')
        for tr in trs:
            name = tr.find('td','name').get_text(strip=True)
            total = tr.find('td','total').get_text(strip=True)
            f.write(name+'\t' + total+'\n')
    except URLError as e:
        print(e)
        return
    except HTTPError as e:
        print(e)
        return

f = open('p2peye/news.txt', 'w', encoding='utf-8')

dfs('http://www.p2peye.com/shuju/ptsj/')