from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().rsplit())


move = (1, 0), (-1, 0), (0, 1), (0, -1)


def is_valid_for_water(y, x, map, visited):
    if 0 <= y < R and 0 <= x < C and (map[y][x] == "." or map[y][x] == "S") and visited[y][x] != 1:
        return True
    return False


def is_valid_for_hedgehog(y, x, map, visited):
    if 0 <= y < R and 0 <= x < C and (map[y][x] == "." or map[y][x] == "D") and not visited[y][x]:
        return True
    return False


forest = [list(input().rstrip()) for _ in range(R)]


visited = [[False] * C for _ in range(R)]

queue = deque([])
water_queue = deque([])
for y in range(R):
    for x in range(C):
        if forest[y][x] == "S":
            queue.append((y, x))
            visited[y][x] = True
            continue
        elif forest[y][x] == "*":
            water_queue.append((y, x))
            visited[y][x] = True
            continue


time = 0
while queue:
    time += 1
    loop_cnt = len(queue)
    water_loop_cnt = len(water_queue)

    for _ in range(water_loop_cnt):
        y, x = water_queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if is_valid_for_water(ny, nx, forest, visited):
                visited[ny][nx] = 1
                water_queue.append((ny, nx))

    for _ in range(loop_cnt):
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x+dx
            if is_valid_for_hedgehog(ny, nx, forest, visited):
                visited[ny][nx] = 2
                queue.append((ny, nx))
                if forest[ny][nx] == "D":
                    print(time)
                    exit()
print("KAKTUS")
