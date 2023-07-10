from sys import stdin

LINE = 9
input = stdin.readline


board = [[0] * LINE for _ in range(LINE)]

for i in range(LINE):
    row = list(map(int, input().split()))
    for j in range(LINE):
        board[i][j] = row[j]


def is_valid(board, row, col, num):
    for i in range(LINE):
        if board[row][i] == num:
            return False

    for i in range(LINE):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(LINE):
        for col in range(LINE):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


solve_sudoku(board)

for row in board:
    print(" ".join(map(str, row)))
