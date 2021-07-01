#!/usr/bin/env python3
import argparse

def app(x):
    print('{0} is a {1}'.format(x, type(x).__name__))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='a very simple app with command line arguments.')
    parser.add_argument('last', help='the last argument')
    args = parser.parse_args()
    app(args.last)
