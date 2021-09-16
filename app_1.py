"""审查元素爬虫
"""
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os


def main():
    site = 'https://pvp.qq.com/web201605/herolist.shtml'
    headers = {
        'user-agent': 'chrome',
        'referer': 'https://pvp.qq.com/'
    }
    resp = requests.get(site, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')  # 构建一个汤
    hero_list = soup.select('ul.herolist li a img')  # 元素定位
    _dir = './heros/'
    os.makedirs(_dir, exist_ok=True)
    for hero in tqdm(hero_list):
        name = hero['alt']
        link = 'https:'+hero['src']
        resp = requests.get(link)
        with open(_dir+name+link[-4:], 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    main()
