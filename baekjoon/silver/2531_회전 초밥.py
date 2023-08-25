from sys import stdin

input = stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

count = [0] * (d + 1)
types = 0
answer = 0

for i in range(k):
    if count[sushi[i]] == 0:
        types += 1
    count[sushi[i]] += 1

if count[c] == 0:
    answer = types + 1
else:
    answer = types

for i in range(1, n):
    count[sushi[i - 1]] -= 1
    if count[sushi[i - 1]] == 0:
        types -= 1
    if count[sushi[(i + k - 1) % n]] == 0:
        types += 1
    count[sushi[(i + k - 1) % n]] += 1

    if count[c] == 0:
        answer = max(answer, types + 1)
    else:
        answer = max(answer, types)

print(answer)
