# python3
import sys
from functools import reduce

n = int(input())
a0 = [-1, -1]

def read(fun=str):
    buf = ''
    while True:
        part = sys.stdin.read(1)
        if part in ' \n':
            break
        buf += part
    return fun(buf)

while n:
    n -= 1
    a = read(int)
    a0.append(a)
    a0.sort()
    a0 = a0[1:]


print (reduce(lambda a, b: a * b, a0))
