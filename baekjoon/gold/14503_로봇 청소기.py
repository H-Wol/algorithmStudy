from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[False] * m for _ in range(n)]
count = 0

while True:
    if not visited[r][c]:
        visited[r][c] = True
        count += 1

    clean = False
    empty_count = 0

    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + directions[d][0], c + directions[d][1]

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] == 0:
            r, c = nr, nc
            clean = True
            break
        elif 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] == 1:
            empty_count += 1

    if not clean:
        back_dir = (d + 2) % 4
        br, bc = r + directions[back_dir][0], c + directions[back_dir][1]

        if 0 <= br < n and 0 <= bc < m and board[br][bc] == 0:
            r, c = br, bc
        else:
            break

    if empty_count == 4:
        br, bc = r - directions[d][0], c - directions[d][1]

        if 0 <= br < n and 0 <= bc < m and board[br][bc] == 0:
            r, c = br, bc
        else:
            break

print(count)
