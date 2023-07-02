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


N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split(" "))))
primes = Eratos(nums[0], nums[-1])
print(len([i for i in nums if i in primes]))
