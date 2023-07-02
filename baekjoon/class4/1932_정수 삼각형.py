from sys import stdin

input = stdin.readline

n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int, input().split(" "))))


def add(before: list, cur: list):
    res = [cur[0] + before[0]]

    for i in range(1, len(cur) - 1):
        res.append(max(cur[i] + before[i - 1], cur[i] + before[i]))

    res.append(cur[-1] + before[-1])

    return res


for i in range(1, n):
    t[i] = add(t[i - 1], t[i])

print(max(t[-1]))
