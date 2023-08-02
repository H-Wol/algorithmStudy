from sys import stdin

input = stdin.readline


def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]


def is_same(matrix1, matrix2, n, m):
    for i in range(n):
        for j in range(m):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True


n, m = map(int, input().split())


matrix_a = [list(map(int, list(input().strip()))) for _ in range(n)]
matrix_b = [list(map(int, list(input().strip()))) for _ in range(n)]

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if matrix_a[i][j] != matrix_b[i][j]:
            flip(matrix_a, i, j)
            count += 1

if is_same(matrix_a, matrix_b, n, m):
    print(count)
else:
    print(-1)
