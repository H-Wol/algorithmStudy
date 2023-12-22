from sys import stdin

input = stdin.readline


def spread_dust():
    new_board = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                spread_amount = board[i][j] // 5
                spread_count = 0

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        new_board[nx][ny] += spread_amount
                        spread_count += 1

                board[i][j] -= spread_amount * spread_count

    for i in range(R):
        for j in range(C):
            board[i][j] += new_board[i][j]


def operate_air_purifier():
    for i in range(air_cleaner[0] - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for j in range(C - 1):
        board[0][j] = board[0][j + 1]
    for i in range(air_cleaner[0]):
        board[i][C - 1] = board[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        board[air_cleaner[0]][j] = board[air_cleaner[0]][j - 1]
    board[air_cleaner[0]][1] = 0

    for i in range(air_cleaner[1] + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for j in range(C - 1):
        board[R - 1][j] = board[R - 1][j + 1]
    for i in range(R - 1, air_cleaner[1], -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        board[air_cleaner[1]][j] = board[air_cleaner[1]][j - 1]
    board[air_cleaner[1]][1] = 0


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


air_cleaner = []
for i in range(R):
    if board[i][0] == -1:
        air_cleaner.append(i)

for _ in range(T):
    spread_dust()
    operate_air_purifier()

result = sum(sum(row) for row in board) + 2
print(result)
