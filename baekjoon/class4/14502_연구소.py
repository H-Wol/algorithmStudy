from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy

input = stdin.readline
N, M = map(int, input().split())

institute = []
visited = []

blank = []
viruses = []
for i in range(N):
    institute.append(list(map(int, input().split())))
    blank.extend([[i, idx] for idx, j in enumerate(institute[-1]) if j < 1])
    viruses.extend([[i, idx] for idx, j in enumerate(institute[-1]) if j > 1])
    visited.append([False for _ in range(M)])

max_cnt = len(blank)
answer = max_cnt


def moveable(y, x):
    return [y + 1, x], [y, x + 1], [y - 1, x], [y, x - 1]


def isMoveable(y, x, map, visited):
    if M > x >= 0 and N > y >= 0 and map[y][x] == 0 and visited[y][x] == False:
        return True
    return False


def BFS(startY, startX, map, visited):
    cur_cnt = 0
    queue = deque([[startY, startX]])
    visited[startY][startX] = True
    while queue:
        curY, curX = queue.popleft()
        for y, x in moveable(curY, curX):
            if isMoveable(y, x, map, visited):
                visited[y][x] = True
                map[y][x] = 3
                queue.append([y, x])
                cur_cnt += 1
    return cur_cnt


for walls in combinations(blank, 3):
    cnt = 0
    cur_institute = deepcopy(institute)

    for wallY, wallX in walls:
        cur_institute[wallY][wallX] = 4
    new_visited = deepcopy(visited)
    for virusY, virusX in viruses:
        cnt += BFS(virusY, virusX, cur_institute, new_visited)
    if cnt < answer:
        answer = cnt

print(max_cnt - answer - 3)
