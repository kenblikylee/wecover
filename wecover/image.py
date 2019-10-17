from PIL import Image
import requests
import re
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
                _warn_print('图片下载失败，请检查图片地址是否可用。网络图片需要增加前缀: "http://", "https://" 或 "//" 。')
                exit(-1)
        except:
            _warn_print('图片下载异常，请检查图片地址是否可用。网络图片需要增加前缀: "http://", "https://" 或 "//" 。')
            exit(-1)
        return Image.open(BytesIO(res.content))
    else:
        return Image.open(image_path)
