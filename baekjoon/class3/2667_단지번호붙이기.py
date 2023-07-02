import sys
from collections import deque
input = sys.stdin.readline

moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]

N = int(input())


def isMoveable(y, x, map, visited):
    if (N > x >= 0 and N > y >= 0 and visited[y][x] == False and map[y][x] == '1'):
        return True
    return False


field = list()
visited = list()
for _ in range(N):
    field.append(list(input().rstrip()))
    visited.append([False for _ in range(N)])


def BFS(y, x, map, visited):
    if not isMoveable(y, x, map, visited):
        return 0
    visited[y][x] = True
    cnt = 1
    queue = deque([[y, x]])
    while queue:
        curY, curX = queue.popleft()
        for y, x in moveable:
            nextY = curY + y
            nextX = curX + x
            if isMoveable(nextY, nextX, map, visited):
                visited[nextY][nextX] = True
                cnt += 1
                queue.append([nextY, nextX])
    return cnt


answers = list()
for y in range(N):
    for x in range(N):
        if res := BFS(y, x, field, visited):
            answers.append(res)

print(len(answers))
answers.sort()
for answer in answers:
    print(answer)
