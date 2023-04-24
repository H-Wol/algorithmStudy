from sys import stdin

input = stdin.readline

N = int(input())

sales = []

for _ in range(N):
    sales.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(3):
        sales[i][j] = min([sales[i - 1][x] + sales[i][j] for x in range(3) if x != j])
print(min(sales[-1]))
