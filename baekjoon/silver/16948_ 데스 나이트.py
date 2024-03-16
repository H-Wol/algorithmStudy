from sys import stdin
from collections import deque
input = stdin.readline

# 나이트가 움직일수 있는 좌표
moveable = [
    [-2, -1],
    [-2, 1],
    [0, -2],
    [0, 2],
    [2, -1],
    [2, 1]
]


def isMoveable(x: int, y: int, board: list) -> bool:
    if 0 <= x < N and 0 <= y < N and board[y][x] == False:
        return True
    return False


def BFS(startY, startX, endY, endX, board):
    queue = deque([[startY, startX]])
    count = 0
    board[startY][startX] = True
    while queue:
        count += 1
        loop_cnt = len(queue)
        for _ in range(loop_cnt):
            curY, curX = queue.popleft()
            if (curY, curX) == (endY, endX):
                return count
            for dy, dx in moveable:
                ny, nx = dy+curY, dx+curX
                if not isMoveable(nx, ny, board):
                    continue
                if (ny, nx) == (endY, endX):
                    return count
                queue.append((ny, nx))
                board[ny][nx] = True
    return -1


N = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().rsplit())
board = [[False for _ in range(N)] for _ in range(N)]

print(BFS(r1, c1, r2, c2, board))
