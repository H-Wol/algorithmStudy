from sys import stdin

input = stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def rotate_array(layer):
    top = left = layer
    bottom = n - 1 - layer
    right = m - 1 - layer

    tmp = arr[top][left]

    for i in range(left, right):
        arr[top][i] = arr[top][i + 1]

    for i in range(top, bottom):
        arr[i][right] = arr[i + 1][right]

    for i in range(right, left, -1):
        arr[bottom][i] = arr[bottom][i - 1]

    for i in range(bottom, top, -1):
        arr[i][left] = arr[i - 1][left]

    arr[top + 1][left] = tmp


for _ in range(r):
    for layer in range(min(n, m) // 2):
        rotate_array(layer)

for row in arr:
    print(*row)
