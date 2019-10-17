from PIL import Image
import requests
import re
from os import path
from io import BytesIO

_url_pattern = re.compile(r'http[s]?:\/\/|\/\/')

def _warn_print(text):
    print('\u001b[31m{}\u001b[0m'.format(text))

def _suc_print(text):
    print('\u001b[32m{}\u001b[0m'.format(text))

def openimg(image_path):
    if _url_pattern.match(image_path):
        try:
            res = requests.get(image_path)
            if res.status_code != 200:
                exit(-1)
        except:
            _warn_print('图片下载异常，请检查图片地址是否可用。网络图片需要增加前缀: "http://", "https://" 或 "//" 。')
            exit(-1)
        img = Image.open(BytesIO(res.content))
        img_filename = path.basename(image_path)
        img.save(img_filename)
        print('download: {}'.format(img_filename))
        return img
    else:
        if path.isfile(image_path):
            return Image.open(image_path)
        else:
            _warn_print('{} 不存在'.format(image_path))
    return
