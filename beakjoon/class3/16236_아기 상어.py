import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y, x, map, shark_size, visited):
    if N > y >= 0 and N > x >= 0 and map[y][x] <= shark_size and visited[y][x] == False:
        return True
    return False


def BFS(y, x, map, visited, size):
    queue = deque([[y, x]])
    visited[y][x] = 0
    standard = 0
    poses = list()
    while queue:
        curY, curX = queue.popleft()
        if visited[curY][curX] > standard:
            if poses != []:
                return min(poses), visited[curY][curX]
            standard = visited[curY][curX]
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, size, visited):
                visited[ny][nx] = visited[curY][curX] + 1
                if 0 < map[ny][nx] < size:
                    poses.append([ny, nx])
                queue.append([ny, nx])
    raise Exception


space = list()
growth = 0
fishes = list()
cur_pos = list()
shark_size = 2
fish_min_size = 0

for i in range(N):
    space.append(line := list(map(int, input().split(" "))))
    if 9 in line:
        cur_pos = [i, line.index(9)]
        space[cur_pos[0]][cur_pos[1]] = 0
    fishes.extend(filter(lambda x: x if (0 < x) else None, line))
# fishes.sort()
times = 0
while True:
    if fishes == []:
        print(times)
        exit()
    fish_min_size = min(fishes)
    visited = [[False for _ in range(N)] for _ in range(N)]
    if fish_min_size >= shark_size:
        print(times)
        exit()
    try:
        cur_pos, time = BFS(cur_pos[0], cur_pos[1], space, visited, shark_size)
    except:
        print(times)
        exit()
    growth += 1
    times += time
    fishes.remove(space[cur_pos[0]][cur_pos[1]])
    space[cur_pos[0]][cur_pos[1]] = 0
    if growth == shark_size:
        shark_size += 1
        growth = 0
