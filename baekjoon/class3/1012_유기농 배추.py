import sys
input = sys.stdin.readline

moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())


def isMovealbe(y, x, map):
    if (M > x >= 0 and N > y >= 0 and map[y][x][0] == True and map[y][x][1] == 0):
        return True
    return False


def BFS(y, x, map):
    isDomain = False
    if (isMovealbe(y, x, map)):
        map[y][x][1] = 1
        queue = [[y, x]]
        isDomain = True
        while (queue):
            pos = queue.pop(0)
            for i in moveable:
                curretY = pos[0] + i[0]
                curretX = pos[1] + i[1]
                if (isMovealbe(curretY, curretX, map)):
                    map[curretY][curretX][1] = 1
                    queue.append([curretY, curretX])
    return isDomain


for _ in range(T):
    M, N, K = map(int, input().split(" "))

    field = [[[0, 0] for _ in range(M)] for _ in range(N)]

    for k in range(K):
        y, x = map(int, input().split(" "))

        field[x][y] = [1, 0]
    cnt = 0
    for x in range(M):
        for y in range(N):
            if BFS(y, x, field):
                cnt += 1

    print(cnt)
