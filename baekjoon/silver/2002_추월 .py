from sys import stdin

input = stdin.readline

N = int(input())
in_order = [input() for _ in range(N)]
out_order = [input() for _ in range(N)]

count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if in_order.index(out_order[i]) > in_order.index(out_order[j]):
            count += 1
            break

print(count)
