import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]

graph_paper = list()
visited_cnt = [[[0, 0] for _ in range(M)]for _ in range(N)]

for _ in range(N):
    graph_paper.append(list(map(int, input().rstrip().split(" "))))


def isMoveable(y, x, visited_cnt):
    if (M > x >= 0 and N > y >= 0 and visited_cnt[y][x][1] == 0):
        return True
    return False


def BFS(y, x, map, visited_cnt):
    if (isMoveable(y, x, visited_cnt)):
        queue = [[y, x]]
        visited_cnt[y][x][1] = 1
        while (queue):
            pos = queue.pop(0)
            for i in moveable:
                currentY = pos[0] + i[0]
                currentX = pos[1] + i[1]
                if (isMoveable(currentY, currentX, visited_cnt)):
                    if map[currentY][currentX] == 1:
                        visited_cnt[currentY][currentX][0] += 1
                        continue
                    visited_cnt[currentY][currentX][1] = 1
                    queue.append([currentY, currentX])


cnt = 0
while True:
    flag = True

    BFS(0, 0, graph_paper, visited_cnt)

    for y in range(N):
        for x in range(M):
            if visited_cnt[y][x][0] > 1:
                graph_paper[y][x] = 0
                flag = False
            visited_cnt[y][x] = [0, 0]
    if flag:
        break
    cnt += 1

print(cnt)
