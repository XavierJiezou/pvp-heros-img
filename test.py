import requests


def down_img(url: str, save_path: str = 'test.jpg'):
    """Download img testing

    Args:
        url (str): The url of a image
        save_path (str, optional): Save path of the downloaded image. Defaults to 'test.jpg'.
    """
    headers = {  # 请求头（可以轻松的突破发爬虫）
        'user-agent': 'chrome',
        'referer': 'https://pic.netbian.com/'
    }
    res = requests.get(url, headers=headers)
    with open(save_path, 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    down_img('https://pic.netbian.com/uploads/allimg/210912/225228-163145834897ce.jpg')
