import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split(" "))


visited = [False] * 101
board = [0] * 101


ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split(" "))
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split(" "))
    snake[u] = v


def BFS(start: int, target: int, map: list, visited: list, ladder: dict, snake: dict):
    visited[start] = True
    queue = deque([start])
    while queue:
        current_pos = queue.popleft()
        for dice in range(1, 7):
            next_pos = current_pos + dice
            if next_pos > target or visited[next_pos]:
                continue
            if next_pos == target:
                print(board[current_pos]+1)
                return
            if x := ladder.get(next_pos, False):
                next_pos = x
            if x := snake.get(next_pos, False):
                next_pos = x
            if not visited[next_pos]:
                visited[next_pos] = True
                map[next_pos] = map[current_pos]+1
                queue.append(next_pos)


BFS(1, 100, board, visited, ladder, snake)
