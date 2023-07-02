from sys import stdin

input = stdin.readline

n = int(input())
sequence = list(map(int, input().split()))


def find_lis(sequence):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def find_lds(sequence):
    dp = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def find_bitonic(sequence):
    lis = find_lis(sequence)
    lds = find_lds(sequence)
    bitonic = [lis[i] + lds[i] - 1 for i in range(n)]

    return max(bitonic)


result = find_bitonic(sequence)
print(result)
