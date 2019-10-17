import sys
import re
import glob
from .image import openimg, makecover

__version__ = '0.1.0'

_arg_pattern = re.compile(r'--\w+|-\w+')

def _parse_args(args_list):
    argk = None
    args = dict()
    targets = list()
    for arg in args_list:
        if _arg_pattern.match(arg):
            argk = arg.strip('-')
            args[argk] = ''
        elif argk:
            args[argk] = arg
            argk = None
        else:
            targets.append(arg)
    return args, targets

def _print_welcom():
    _print_run()
    print('\u001b[32m使用:\u001b[0m wecover <title> [logo_path|logo_url]')

def _print_run():
    print('\u001b[1mwecover v{}\u001b[0m'.format(__version__))
    print('\u001b[4mhttps://github.com/kenblikylee/wecover\u001b[0m')

def _is_image(img):
    return re.search('\.(jpg|jpeg|png)$', img)

def _auto_search_log():
    logos = glob.glob('./logo.*')
    for logo in logos:
        if re.search('logo\.(jpg|jpeg|png)$', logo):
            return logo
    return None

def _warn_print(text):
    print('\u001b[31m{}\u001b[0m'.format(text))

def run(params):
    args, targets = params

    # 读取标题
    title = None
    if 'title' in args:
        title = args['title']
    elif 't' in args:
        title = args['t']
    elif len(targets):
        title = targets[0]

    if not title:
        _warn_print('请提供封面标题')
        exit(-1)
    print('title: {}'.format(title))

    # 读取 logo
    logo = None
    if 'logo' in args:
        logo = args['logo']
    elif 'l' in args:
        logo = args['l']
    elif len(targets) > 1:
        logo = targets[1]
    else:
        logo = _auto_search_log()

    if logo:
        print('logo: {}'.format(logo))
        if _is_image(logo):
            logo = openimg(logo)
        else:
            _warn_print('logo 图片格式只支持: .jpg .jpeg .png'.format(logo))
            logo = None
        if logo:
            print('size: {}*{}'.format(*logo.size))

    makecover(title, logo)

def main():
    cmds = sys.argv[1:]
    if len(cmds) == 0:
        _print_welcom()
    else:
        _print_run()
        run(_parse_args(cmds))
