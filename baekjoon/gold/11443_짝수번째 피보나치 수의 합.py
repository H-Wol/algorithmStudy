def matrix_multi(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += (A[i][j] * B[j][k]) % 1_000_000_007
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

N = int(stdin.readline())
if N % 2 == 0:
    N = N + 1
print((matrix_pow([[1, 1], [1, 0]], N)[0][1] - 1) % 1_000_000_007)
