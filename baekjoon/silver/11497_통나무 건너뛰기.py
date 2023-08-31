from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    logs = list(map(int, input().split()))
    logs.sort()

    max_diff = 0
    for i in range(2, n):
        max_diff = max(max_diff, abs(logs[i] - logs[i-2]))

    print(max_diff)
