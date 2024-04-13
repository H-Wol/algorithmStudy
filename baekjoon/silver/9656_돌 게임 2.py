from sys import stdin

input = stdin.readline

N = int(input().strip())

if N % 2 == 1:
    print("CY")
else:
    print("SK")
