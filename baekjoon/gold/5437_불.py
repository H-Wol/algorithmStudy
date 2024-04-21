from collections import deque
from sys import stdin

input = stdin.readline


def bfs(fire_queue, person_queue, visited, maps, w, h):
    time = 0

    while person_queue:
        fire_size = len(fire_queue)
        for _ in range(fire_size):
            fy, fx = fire_queue.popleft()

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = fy + dy, fx + dx
                if (
                    0 <= ny < h
                    and 0 <= nx < w
                    and (maps[ny][nx] == "." or maps[ny][nx] == "@")
                ):
                    maps[ny][nx] = "*"
                    fire_queue.append((ny, nx))

        person_size = len(person_queue)
        for _ in range(person_size):
            y, x = person_queue.popleft()

            if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                return time + 1

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if (
                    0 <= ny < h
                    and 0 <= nx < w
                    and maps[ny][nx] == "."
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    person_queue.append((ny, nx))

        time += 1

    return "IMPOSSIBLE"


t = int(input().strip())
results = []

for _ in range(t):
    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(h)]
    fire_queue = deque()
    person_queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == "*":
                fire_queue.append((i, j))
            elif maps[i][j] == "@":
                person_queue.append((i, j))
                visited[i][j] = True

    result = bfs(fire_queue, person_queue, visited, maps, w, h)
    results.append(result)

for res in results:
    print(res)
