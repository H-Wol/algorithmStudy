import sys
import re

N = int(sys.stdin.readline())

pat = re.compile("[1-9]")


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


print(len(re.split(pat, str(factorial(N)))[-1]))
