from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
right = 0
count = 0
min_len = float('inf')

while right < N:
    if dolls[right] == 1:
        count += 1

    while count == K:
        min_len = min(min_len, right - left + 1)
        if dolls[left] == 1:
            count -= 1
        left += 1

    right += 1

if min_len == float('inf'):
    print(-1)
else:
    print(min_len)
