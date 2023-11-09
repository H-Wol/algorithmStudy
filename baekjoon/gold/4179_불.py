from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().rsplit())


move = (1, 0), (-1, 0), (0, 1), (0, -1)


def is_valid_for_fire(y, x, map, visited):
    if 0 <= y < R and 0 <= x < C and map[y][x] != "#" and visited[y][x] != 1:
        return True
    return False


def is_valid_for_jihoon(y, x, map, visited):
    if 0 <= y < R and 0 <= x < C and map[y][x] == "." and not visited[y][x]:
        return True
    return False


maze = [list(input().rstrip()) for _ in range(R)]


visited = [[False] * C for _ in range(R)]

queue = deque([])
fire_queue = deque([])
for y in range(R):
    for x in range(C):
        if maze[y][x] == "J":
            queue.append((y, x))
            visited[y][x] = True
        elif maze[y][x] == "F":
            fire_queue.append((y, x))
            visited[y][x] = True
        elif maze[y][x] == "#":
            visited[y][x] = True


time = 0
while queue:
    time += 1
    loop_cnt = len(queue)
    fire_loop_cnt = len(fire_queue)

    for _ in range(fire_loop_cnt):
        y, x = fire_queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if is_valid_for_fire(ny, nx, maze, visited):
                visited[ny][nx] = 1
                fire_queue.append((ny, nx))

    for _ in range(loop_cnt):
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x+dx
            if ny < 0 or ny == R or nx < 0 or nx == C:
                print(time)
                exit()
            if is_valid_for_jihoon(ny, nx, maze, visited):
                visited[ny][nx] = 2
                queue.append((ny, nx))


print("IMPOSSIBLE")
