"""API接口爬虫（捷径）
"""
import requests
import os
from tqdm import tqdm


def main():
    api = 'https://pvp.qq.com/web201605/js/herolist.json'
    res = requests.get(api).json()  # .json()方法转为字典
    tmp = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{ename}/{ename}.jpg'
    dir = './heros/'
    os.makedirs(dir, exist_ok=True)
    for item in tqdm(res):
        ename = item['ename']
        cname = item['cname']
        url = tmp.format(ename=ename)
        res = requests.get(url)
        with open(dir+cname+url[-4:], 'wb') as f:
            f.write(res.content)


if __name__ == '__main__':
    main()
