from sys import stdin
from math import gcd

input = stdin.readline


A, B = map(int, input().split())


print(A * B // gcd(A, B))
