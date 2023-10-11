from sys import stdin
from collections import deque

input = stdin.readline

M = int(input())
game_map = []
game_map.append(list(input().rstrip()))
game_map.append(list(input().rstrip()))
white_num = sum(line.count(".") for line in game_map)
visited = [[False for _ in range(M)] for _ in range(2)]
if M == 1:
    if game_map[0][0] == game_map[1][0] == ".":
        print(1)
    else:
        print(0)
    exit()


def is_moveAble(y: int, x: int, game_map: list, visited: list):
    if 0 <= y <= 1 and 0 <= x < M and game_map[y][x] != "#" and visited[y][x] == False:
        return True
    return False


def bfs(game_map: list, visited: list):
    queue = deque((y, x) for y, x in [(0, 0), (1, 0)] if game_map[y][x] == ".")
    for y, x in queue:
        visited[y][x] = True
    count = 1
    while queue:
        count += 1
        current_queue_length = len(queue)
        for _ in range(current_queue_length):
            cur_y, cur_x = queue.popleft()
            for dy, dx in [(1, 0), (-1, 0), (0, 1)]:
                ny, nx = cur_y + dy, cur_x + dx
                if not is_moveAble(ny, nx, game_map, visited):
                    continue
                if nx == M - 1:
                    return count
                queue.append((ny, nx))
                visited[ny][nx] = True


print(white_num - bfs(game_map, visited))
