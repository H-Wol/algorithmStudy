from sys import stdin

input = stdin.readline


def check_max_candy(board):
    max_candy = 1

    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                count += 1
            else:
                max_candy = max(max_candy, count)
                count = 1
        max_candy = max(max_candy, count)

    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                max_candy = max(max_candy, count)
                count = 1
        max_candy = max(max_candy, count)

    return max_candy


def swap(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]


def find_max_candy(board):
    max_candy = 0

    for i in range(N):
        for j in range(N):

            if j + 1 < N and board[i][j] != board[i][j + 1]:
                swap(board, i, j, i, j + 1)
                max_candy = max(max_candy, check_max_candy(board))
                swap(board, i, j, i, j + 1)

            if i + 1 < N and board[i][j] != board[i + 1][j]:
                swap(board, i, j, i + 1, j)
                max_candy = max(max_candy, check_max_candy(board))
                swap(board, i, j, i + 1, j)

    return max_candy


N = int(input())
board = [list(input().strip()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):

        if j + 1 < N and board[i][j] != board[i][j + 1]:
            swap(board, i, j, i, j + 1)
            result = max(result, check_max_candy(board))
            swap(board, i, j, i, j + 1)

        if i + 1 < N and board[i][j] != board[i + 1][j]:
            swap(board, i, j, i + 1, j)
            result = max(result, check_max_candy(board))
            swap(board, i, j, i + 1, j)

print(result)
