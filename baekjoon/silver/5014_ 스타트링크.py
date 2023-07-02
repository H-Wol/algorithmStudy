from sys import stdin

F, S, G, U, D = map(int, stdin.readline().split())


def moveable(x):
    return x + U, x - D


from collections import deque

maps = [0] * (F + 1)


def BFS(start, end, maps):
    maps[start] = 1
    if start == end:
        return 0
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for i in moveable(cur):
            if i < 1 or i > F:
                continue
            if i == end:
                return maps[cur]
            if maps[i] == 0:
                maps[i] = maps[cur] + 1
                queue.append(i)
    return "use the stairs"


print(BFS(S, G, maps))
