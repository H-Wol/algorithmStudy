from sys import stdin

input = stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

min_cost = float('inf')


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]


def calculate_total_cost(flowers):
    total_cost = 0
    visited_flowers = []

    for flower in flowers:
        x, y = flower
        visited_flowers.append((x, y))
        total_cost += cost[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            visited_flowers.append((nx, ny))
            total_cost += cost[nx][ny]

    return total_cost, visited_flowers


def dfs(count, flowers):
    global min_cost

    if count == 3:
        total_cost, visited_flowers = calculate_total_cost(flowers)

        if len(visited_flowers) == len(set(visited_flowers)):
            min_cost = min(min_cost, total_cost)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if is_valid(i, j):
                visited[i][j] = True
                flowers.append((i, j))
                dfs(count + 1, flowers)
                flowers.pop()
                visited[i][j] = False


dfs(0, [])

print(min_cost)
