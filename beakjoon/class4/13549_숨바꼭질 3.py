from sys import stdin
from collections import deque


maps = [float("inf") for _ in range(200_002)]
visited = [False for _ in range(200_002)]
N, K = map(int, stdin.readline().split())


def moveable(x: int):
    return (x * 2, 0), (x + 1, 1), (x - 1, 1)


def BFS(start, end, maps, visited):
    if start == end:
        return [0]
    queue = deque([start])
    maps[start] = 0
    ans = set()
    flag = True
    while queue and flag:
        step = len(queue)
        for _ in range(step):
            cur = queue.popleft()
            for next, val in moveable(cur):
                if 200_001 < next or next < 0 or visited[next]:
                    continue
                if next == end:
                    ans.add(maps[cur] + val)
                    flag = False
                    continue
                maps[next] = min(maps[next], maps[cur] + val)
                visited[next] = True
                if val:
                    queue.append(next)
                else:
                    step += 1
                    queue.appendleft(next)
    return ans


print(min(BFS(N, K, maps, visited)))
