from sys import stdin

input = stdin.readline

T = int(input())

default = [1, 1, 1, 2, 2]
for _ in range(T):
    N = int(input())
    for i in range(len(default), N + 1, 1):
        default.append(default[i - 5] + default[-1])
    print(default[N - 1])
