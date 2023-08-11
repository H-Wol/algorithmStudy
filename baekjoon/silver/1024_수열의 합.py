n, l = map(int, input().split())

while l <= 100:
    start = n // l - (l - 1) // 2

    if start < 0:
        l += 1
        continue

    seq_sum = (2 * start + l - 1) * l // 2

    if seq_sum == n:
        for i in range(l):
            print(start + i, end=" ")
        break
    l += 1

else:
    print(-1)
