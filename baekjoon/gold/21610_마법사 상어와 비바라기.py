from sys import stdin

input = stdin.readline


def count_pills(W, H, memo):
    if W == 0:
        return 1
    if memo[W][H] != -1:
        return memo[W][H]

    result = 0
    if W > 0:
        result += count_pills(W - 1, H + 1, memo)
    if H > 0:
        result += count_pills(W, H - 1, memo)

    memo[W][H] = result
    return result


while True:
    N = int(input())
    if N == 0:
        break

    memo = [[-1] * (N + 1) for _ in range(N + 1)]
    result = count_pills(N, 0, memo)
    print(result)
