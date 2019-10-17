from PIL import Image, ImageDraw, ImageFont
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

def square(image):
    w, h = image.size
    if w == h: return image
    short_edge = min(w, h)
    if short_edge == w:
        offset = round((h - w) / 2)
        crop_box = (0, offset, short_edge, offset+short_edge)
    else:
        offset = round((w - h) / 2)
        crop_box = (offset, 0, offset+short_edge, short_edge)
    return image.crop(crop_box)

def resize(image, size):
    if image.size[0] <= size[0]:
        return image
    return image.resize(size)

def process_logo(logo, logo_size):
    sqlogo = square(logo)
    if logo.size[0] != logo.size[1]:
        print('crop to: {}*{}'.format(*sqlogo.size))
    if sqlogo.size[0] > logo_size[0]:
        print('resize to: {}*{}'.format(*logo_size))
    rzlogo = resize(sqlogo, logo_size)
    return rzlogo

def create_canvas(size, color='white'):
    return Image.new('RGB', size, color)

def load_font(font_size=50):
    macfont = 'PingFang.ttc'
    # heitifont = 'STHeiti Medium.ttc'
    winfont = 'msyh.ttc'
    # winfont = 'msyhbd.ttc'
    try:
        # 加载系统字体
        # macOS
        # - /Library/Fonts/
        # - /System/Library/Fonts/
        # - ~/Library/Fonts/
        font = ImageFont.truetype(macfont, font_size, encoding='unic')
    except OSError as err:
        # _warn_print('系统缺少字体"{}"(苹方)'.format(macfont))
        # _suc_print('使用字体"{}"(微软雅黑)替代'.format(winfont))
        try:
            font = ImageFont.truetype(winfont, font_size, encoding='unic')
        except OSError as err:
            _warn_print('OSError: 系统缺少字体 "{}"(微软雅黑)'.format(winfont))
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    return font

def makecover(title, logo=None, color='#000', bgcolor='#fff', logo_size=(120, 120), cover_height=400):
    cover_width = round(cover_height * 2.35)
    cover_size = (cover_width, cover_height)
    print('cover size: {}*{}'.format(*cover_size))
    canvas = create_canvas(cover_size, bgcolor)

    draw = ImageDraw.Draw(canvas)
    # 绘制标题
    font = load_font(40)
    try:
        title_width, title_height = font.getsize(title)
    except UnicodeEncodeError:
        _warn_print('UnicodeEncodeError: 当前字体不支持中文')
        exit(-1)
    print('title size: {}*{}'.format(title_width, title_height))
    title_y = round((cover_height - title_height)/2)
    title_x = round((cover_width - title_width)/2)

     # 粘贴 LOGO
    if logo:
        logo = process_logo(logo, logo_size)
        logo_width, logo_height = logo.size
        # logo.save('wecover_logo_{}_{}.png'.format(logo_width, logo_height))
        # 图文总宽
        gap = 20
        all_width = logo_width + gap + title_width

        logo_y = round((cover_height - logo_height)/2)
        logo_x = round((cover_width - all_width)/2)
        logo_position = (logo_x, logo_y)
        canvas.paste(logo, logo_position)

        title_x = logo_x + logo_width + gap

    title_position = (title_x, title_y)
    draw.text(title_position, title, fill=color, font=font)
    # draw.multiline_text(title_position, title, fill=color, font=font, spacing=10, align='center')
    canvas.show()
    canvas.save('wecover_'+title+'.jpg')