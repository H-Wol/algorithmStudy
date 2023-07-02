from sys import stdin

input = stdin.readline
R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]

max_cnt, cur_cnt = 0, 0
routes = [True] * 26


def DFS(y, x):
    global max_cnt, cur_cnt
    cur_cnt += 1
    max_cnt = max(max_cnt, cur_cnt)
    routes[ord(board[y][x]) - 65] = False
    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and routes[ord(board[ny][nx]) - 65]:
            DFS(ny, nx)
            routes[ord(board[ny][nx]) - 65] = True
            cur_cnt -= 1


DFS(0, 0)
print(max_cnt)
