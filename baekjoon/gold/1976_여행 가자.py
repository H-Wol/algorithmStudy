from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, n + 1):
        if data[j - 1] == 1:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

result = True


for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
