import sys
moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

N, M, K = map(int, input().split())

# 입력 받은 영역의 map 생성 (이동 가능 여부, 방문 여부)
maps = [[[True, 0] for _ in range(M)] for _ in range(N)]
sizes = []  # 영역 사이즈 리스트
size = 0  # DFS에서 사용할 전역 size


def isMovealbe(y, x, map):
    if (M > x >= 0 and N > y >= 0 and map[y][x][0] == True and map[y][x][1] == 0):
        return True
    return False


def DFS(y, x, map):
    global size
    if (isMovealbe(y, x, map)):
        map[y][x][1] = 1
        size += 1
        for i in moveable:
            if (isMovealbe(y+i[0], x+i[1], map)):
                DFS(y+i[0], x+i[1], map)


for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            maps[y][x][0] = False

for y in range(N):
    for x in range(M):
        DFS(y, x, maps)
        if (size > 0):
            sizes.append(size)
            size = 0

print(len(sizes))

for n in sorted(sizes):
    print(n, end=' ')
