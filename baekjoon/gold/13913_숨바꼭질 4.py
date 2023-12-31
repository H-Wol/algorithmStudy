from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**5)

N, K = map(int, stdin.readline().split())
maps = [False for _ in range(200_002)]
visited = [False for _ in range(200_002)]


def moveable(x: int):
    return x * 2, x + 1, x - 1


def BFS(start, end, maps):
    if start == end:
        return 0, start, maps
    queue = deque([start])
    count = 0
    maps[start] = -1
    visited[start] = True
    while queue:
        count += 1
        step = len(queue)
        for _ in range(step):
            cur = queue.popleft()
            for next in moveable(cur):
                if 200_000 < next or next < 0 or visited[next]:
                    continue
                maps[next] = cur
                visited[next] = True
                if next == end:
                    return count, end, maps
                queue.append(next)
    return count, end, maps


count, end, maps = BFS(N, K, maps)


def get_routes(cur):
    if maps[cur] != -1:
        get_routes(maps[cur])
    print(cur, end=" ")


print(count)
if count == 0:
    print(end)
    exit()
get_routes(end)
