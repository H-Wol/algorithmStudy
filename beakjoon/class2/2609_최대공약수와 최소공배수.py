
import sys


def uclid(a, b):
    return a if b == 0 else uclid(b, a % b)


a, b = map(int, sys.stdin.readline().split(" "))
if a < b:
    t = a
    a = b
    b = t

GCD = uclid(a, b)

print(GCD)
print(int(a*b/GCD))
