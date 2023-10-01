from sys import stdin

input = stdin.readline
x, y = map(int, input().split())
current_win_rate = y * 100 // x
left, right = 1, 1000000000
result = -1

while left <= right:
    mid = (left + right) // 2
    new_win_rate = ((y + mid) * 100) // (x + mid)

    if new_win_rate > current_win_rate:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)
