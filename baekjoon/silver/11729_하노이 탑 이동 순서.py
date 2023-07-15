n = int(input())

res = []


def hanoi(n, start, end, aux):
    if n == 1:
        res.append([start, end])
    else:
        hanoi(n - 1, start, aux, end)
        res.append([start, end])
        hanoi(n - 1, aux, end, start)


hanoi(n, 1, 3, 2)
print(len(res))
for a, b in res:
    print(a, b)
