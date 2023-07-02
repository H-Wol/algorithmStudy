from sys import stdin


def tetromino(board, x, y):
    tetrominos = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 2), (1, 1), (1, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (1, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (1, 1), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (0, 1), (0, 2)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 0)],
        [(0, 1), (1, 1), (1, 0), (2, 1)],
    ]

    max_sum = 0
    for shape in tetrominos:
        sum = 0
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                sum += board[nx][ny]
            else:
                sum = 0
                break
        max_sum = max(max_sum, sum)
    return max_sum


input = stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, tetromino(board, i, j))

print(result)
