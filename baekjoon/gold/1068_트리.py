from sys import stdin

input = stdin.readline


n = int(input())
parent = list(map(int, input().split()))
removed = int(input())

tree = [[] for _ in range(n)]
root = -1


def dfs(num, parent):
    parent[num] = -2
    for i in range(len(parent)):
        if num == parent[i]:
            dfs(i, parent)


dfs(removed, parent)
count = 0
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        count += 1
print(count)
