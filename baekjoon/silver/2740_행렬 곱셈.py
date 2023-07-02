def matrix_multi(a, b):
    temp = [[0] * (len(b[0])) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                temp[i][k] += a[i][j] * b[j][k]
    return temp


from sys import stdin

input = stdin.readline
A = []
B = []
N, M = map(int, input().split())

for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

for i in matrix_multi(A, B):
    print(" ".join(map(str, i)))
