from sys import stdin

input = stdin.readline
n = int(input())
scores = [int(input()) for _ in range(n)]
result = 0
for i in range(n-2, -1, -1):
    if scores[i] >= scores[i+1]:
        diff = scores[i] - scores[i+1] + 1
        result += diff
        scores[i] -= diff

print(result)
