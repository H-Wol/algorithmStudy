from sys import stdin
from collections import deque

input = stdin.readline

N, M, K = map(int, input().split())
answer = 0
floor, visited = [[True for _ in range(M)] for _ in range(N)], [[False for _ in range(M)] for _ in range(N)]
foods = []

for _ in range(K):
    foody, foodx = map(int, input().split())
    floor[foody - 1][foodx - 1] = False
    foods.append([foody - 1, foodx - 1])


def moveable(y, x):
    return (y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)


def is_possible(y, x, visited, map):
    if 0 <= y < N and 0 <= x < M and visited[y][x] == False and map[y][x] == False:
        return True
    return False


def bfs(starty, startx, map, visited):
    if visited[starty][startx] == True:
        return 0, visited
    queue = deque([[starty, startx]])
    cnt = 0
    while queue:
        cury, curx = queue.popleft()
        for y, x in moveable(cury, curx):
            if is_possible(y, x, visited, map):
                visited[y][x] = True
                queue.append([y, x])
                cnt += 1
    return cnt, visited


for food in foods:
    cnt, visited = bfs(food[0], food[1], floor, visited)
    answer = max(answer, cnt)
print(answer)
