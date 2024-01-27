from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
withdrawals = [int(input()) for _ in range(N)]
low, high = max(withdrawals), sum(withdrawals)

while low <= high:
    mid = (low + high) // 2
    count = 1
    current_money = mid

    for withdrawal in withdrawals:
        if current_money < withdrawal:
            count += 1
            current_money = mid
        current_money -= withdrawal

    if count <= M:
        high = mid - 1
    else:
        low = mid + 1

print(low)
