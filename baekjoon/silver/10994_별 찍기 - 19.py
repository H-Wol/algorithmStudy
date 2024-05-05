from sys import stdin

input = stdin.readline


N = int(input())
size = 4 * N - 3


stars = [[" "] * size for _ in range(size)]


def draw_stars(n, start_row, start_col):
    if n == 1:
        stars[start_row][start_col] = "*"
        return

    size = 4 * n - 3

    for i in range(start_col, start_col + size):
        stars[start_row][i] = "*"
        stars[start_row + size - 1][i] = "*"
    for i in range(start_row, start_row + size):
        stars[i][start_col] = "*"
        stars[i][start_col + size - 1] = "*"

    draw_stars(n - 1, start_row + 2, start_col + 2)


draw_stars(N, 0, 0)


for row in stars:
    print("".join(row))
