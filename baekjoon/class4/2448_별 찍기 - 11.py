def draw_stars(n):
    stars = [[" " for _ in range(2 * n)] for _ in range(n)]

    def fill_star(x, y, size):
        if size == 3:
            stars[x][y] = "*"
            stars[x + 1][y - 1] = stars[x + 1][y + 1] = "*"
            stars[x + 2][y - 2 : y + 3] = ["*", "*", "*", "*", "*"]
        else:
            next_size = size // 2
            fill_star(x, y, next_size)
            fill_star(x + next_size, y - next_size, next_size)
            fill_star(x + next_size, y + next_size, next_size)

    fill_star(0, n - 1, n)

    for line in stars:
        print("".join(line))


N = int(input())

draw_stars(N)
