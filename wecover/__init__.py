import sys
import re

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
    print('=========================================\nHi, guy! Welcome to use wecover v{} !\nhttps://github.com/kenblikylee/wecover\n-----------------------------------------'.format(__version__))

def _print_run():
    print('run wecover v{} ...'.format(__version__))

def run(params):
    args, targets = params
    print('args', args)
    print('targets', targets)

def main():
    cmds = sys.argv[1:]
    if len(cmds) == 0:
        _print_welcom()
    else:
        _print_run()
        run(_parse_args(cmds))
