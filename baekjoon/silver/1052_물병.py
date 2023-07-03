from sys import stdin

n, k = map(int, stdin.readline().split())

answer = 0
while bin(n).count("1") > k:
    idx = bin(n)[::-1].index("1")
    diff = 2**idx
    answer += diff
    n += diff

print(answer)
