from sys import stdin

input = stdin.readline

N, L = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

for height in heights:
    if height <= L:
        L += 1

print(L)
