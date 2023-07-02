import sys
import math


def Eratos(start, end):
    if end < 2:
        return []
    if end == 2:
        return [2]
    if end < start:
        return []
    if start == 1:
        start = 2

    n = int(end**0.5)

    primes = [True for i in range(start, end+1)]

    for i in range(2, n+1):
        if i >= start and not primes[i-start]:
            continue
        fromNum = start
        if start > i:
            fromNum = math.ceil(start / i)
        for j in range(i * fromNum, end+1, i):
            primes[j-start] = False

    return [i for i in range(start, end+1) if primes[i-start]]


M, N = map(int, sys.stdin.readline().split())
res = Eratos(M, N)

for i in res:
    print(i)
