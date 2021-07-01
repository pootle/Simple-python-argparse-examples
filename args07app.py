#!/usr/bin/env python3
import argparse, pathlib

def myapp(integer, operands):
    accum=(int if integer else float)(operands.pop(0))
    nextop='+'
    numparse=int if integer else float
    while len(operands) > 0:
        op = operands.pop(0)
        if op in ('+', '-', 'x', '/'):
            nextop = op
        else:
            v=numparse(op)
            if nextop=='+':
                accum += v
            elif nextop=='-':
                accum -= v
            elif nextop=='x':
                accum *= v
            elif nextop=='/':
                if integer:
                    accum //= v
                else:
                    accum /= v
       
    print(accum)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mr Calculate')
    parser.add_argument('-i', '--integer', action='store_true', help= 'force integer arithmetic')
    parser.add_argument('operands', nargs='+', help='list of numbers')
    args = parser.parse_args()
#    print(args.__dict__)
    myapp(**args.__dict__)
