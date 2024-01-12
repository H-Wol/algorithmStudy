

from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
queries = [list(map(int, input().split())) for _ in range(k)]


def partial_sum_2d(n, m, arr, k, queries):
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i -
                                                              1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

    result = []
    for query in queries:
        i, j, x, y = query
        partial_sum = prefix_sum[x][y] - prefix_sum[i - 1][y] - \
            prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
        result.append(partial_sum)

    return result


result = partial_sum_2d(n, m, arr, k, queries)
for res in result:
    print(res)
