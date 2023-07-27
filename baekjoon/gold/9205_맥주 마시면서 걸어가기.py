from sys import stdin
from collections import deque

input = stdin.readline


def bfs(start, end, stores):
    queue = deque([start])
    visited = set()

    while queue:
        x, y = queue.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return "happy"

        for store in stores:
            dist = abs(x - store[0]) + abs(y - store[1])
            if dist <= 1000 and store not in visited:
                queue.append(store)
                visited.add(store)

    return "sad"


t = int(input())

for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    end = tuple(map(int, input().split()))

    result = bfs(start, end, stores)
    print(result)
