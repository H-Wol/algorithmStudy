n = int(input())

counts = []


def squares(n, cnt):
    if cnt > 4 or n < 0:
        return 0
    sqrt = int(n**0.5)
    if sqrt**2 == n:
        counts.append(cnt)
        return 0
    for i in range(sqrt, int(sqrt // 2), -1):
        next_num = n - i**2
        squares(next_num, cnt + 1)


squares(n, 1)

print(min(set(counts)))
