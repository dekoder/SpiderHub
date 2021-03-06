# -*- coding:utf8 -*-
import urllib
from bs4 import BeautifulSoup
import re


def get_all_url(url):
    urls = set()
    web = urllib.urlopen(url)
    soup = BeautifulSoup(web.read())
    # 通过正则过滤合理的url(针对与freebuf.com来讲)
    tags_a = soup.findAll(name='a', attrs={'href': re.compile("^https?://")})
    try:
        for tag_a in tags_a:
            urls.add(tag_a['href'])
    except:
        pass
    return urls


# 得到所有freebuf.com下的url
def get_local_urls(url):
    local_urls = set()
    urls = get_all_url(url)
    for _url in urls:
        ret = _url
        if 'freebuf.com' in ret.replace('//', '').split('/')[0]:
            local_urls.add(_url)
    return local_urls


# 得到所有的不是freebuf.com域名的url
def get_remote_urls(url):
    remote_urls = set()
    urls = get_all_url(url)
    for _url in urls:
        ret = _url
        if "freebuf.com" not in ret.replace('//', '').split('/')[0]:
            remote_urls.add(_url)
    return remote_urls


def __main__():
    url = 'http://freebuf.com/'
    rurls = get_remote_urls(url)
    print "--------------------remote urls-----------------------"
    for ret in rurls:
        print ret
    print "---------------------local urls-----------------------"
    lurls = get_local_urls(url)
    for ret in lurls:
        print ret


if __name__ == '__main__':
    __main__()
