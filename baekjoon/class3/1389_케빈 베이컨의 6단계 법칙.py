import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))

nodes = [[]for _ in range(N+1)]


for _ in range(M):
    x, y = map(int, input().split(" "))
    nodes[x].append(y)
    nodes[y].append(x)


def BFS(start, map, visited):
    cnt = 0
    visited[start] = 1
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for x in map[cur]:
            if visited[x] == 0:
                visited[x] = visited[cur] + 1
                cnt += visited[x]
                queue.append(x)
    return cnt


min_cnt = sys.maxsize
answer = 1
for i in range(N, 0, -1):
    visited = [0] * (N+1)
    cnt = BFS(i, nodes, visited)
    if cnt <= min_cnt:
        min_cnt = cnt
        answer = i

print(answer)
