from sys import stdin
from math import ceil

A, B, V = map(int, stdin.readline().split(" "))

print(1 + ceil((V - A) / (A-B)))
