import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nodes = dict()

def addFunc(list:list, att):
    list.append(att)
    return list

for _ in range(N - 1):
    x, y = map(int, input().split(" "))
    nodes[x] = addFunc(nodes.get(x, list()), y)
    nodes[y] = addFunc(nodes.get(y, list()), x)

visited = {1: 0}
queue = deque([1])

while queue:
    cur = queue.popleft()
    for x in nodes.get(cur):
        if visited.get(x, None) == None:
            visited[x] = cur
            queue.append(x)


for i in range(1, N, 1):
    print(visited[i + 1])
