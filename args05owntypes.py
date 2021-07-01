#!/usr/bin/env python3
import argparse, pathlib

def info(name, x):
    return '{0:15s}:{1} is a {2}'.format(name, x, type(x).__name__)

def input_file(fn):
    fp=pathlib.Path(fn)
    if fp.is_file():
        return fp
    else:
        raise ValueError()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='a very simple app with command line arguments.')
    parser.add_argument('-u', '--upper', action='store_true', help="convert strings to upper case if present - default off")
    parser.add_argument('-s', '--set_false', action='store_false', help='this argument defaults to True')
                # there are other actions - see https://docs.python.org/3/library/argparse.html#action
    parser.add_argument('files', nargs='+', type=input_file, help='the last argument, zero or more')        
                # use nargs='+' to force at least 1
                # use nargs='*' for zero or more
                # use nargs=5   for exactly 5
    
    args = parser.parse_args()
    print(info('upper', args.upper))
    print(info('set_false', args.set_false))
    print(info('files', args.files))

