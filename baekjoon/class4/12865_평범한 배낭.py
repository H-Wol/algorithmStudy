from sys import stdin

input = stdin.readline

N, K = map(int, input().split(" "))

arr = [[0] * (K + 1) for _ in range(N + 1)]


stuff = [[0, 0]]

for _ in range(N):
    stuff.append(list(map(int, input().split(" "))))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = stuff[i][0]
        val = stuff[i][1]
        if w > j:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(val + arr[i - 1][j - w], arr[i - 1][j])
print(arr[N][K])
