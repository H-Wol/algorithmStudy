from sys import stdin

input = stdin.readline
t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    while k < M * N:
        if k % N == y:
            print(k + 1)
            break
        k += M
    else:
        print(-1)
