def matrix_multi(a, b):
    temp = [[0] * (len(a)) for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                temp[i][k] += (a[i][j] * b[j][k]) % 1000
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n // 2)
        return matrix_multi(temp, temp)
    else:
        temp = matrix_pow(A, n - 1)
        return matrix_multi(temp, A)


from sys import stdin

input = stdin.readline
matrix = []

N, B = map(int, input().split())

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in matrix_pow(matrix, B):
    print(" ".join((map(str, [j % 1000 for j in i]))))
