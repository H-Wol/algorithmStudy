from sys import stdin

input = stdin.readline


def find_largest_square(n, m, grid):
    max_side_length = min(n, m)
    result = 1

    for i in range(n):
        for j in range(m):
            for k in range(1, max_side_length):
                if i + k < n and j + k < m:
                    if grid[i][j] == grid[i + k][j] == grid[i][j + k] == grid[i + k][j + k]:
                        result = max(result, (k + 1) ** 2)

    return result


n, m = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

print(find_largest_square(n, m, grid))
