import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def is_valid(y, x, map, visited):
    if 0 <= y < H and 0 <= x < W and not visited[y][x] and map[y][x] == '#':
        return True
    return False


def dfs(y, x):
    visited[y][x] = True

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if is_valid(ny, nx, grid, visited):
            dfs(ny, nx)


T = int(input().strip())

for _ in range(T):
    H, W = map(int, input().strip().split())
    grid = [input().strip() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    count = 0

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and grid[i][j] == '#':
                dfs(i, j)
                count += 1

    print(count)
