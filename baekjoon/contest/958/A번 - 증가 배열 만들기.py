import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))

moveable = [[1, 0], [0, 1]]

# num, visited
arrays = [[0 for _ in range(M)]for _ in range(N)]

arrays[0][0] = 1


def isMoveable(y, x):
    if (M > x >= 0 and N > y >= 0):
        return True
    return False


def BFS(y, x, map, max):
    failFlag = False
    queue = deque([[y, x]])
    while (not failFlag and queue):
        y, x = queue.popleft()
        for i in moveable:
            currentY = y + i[0]
            currentX = x + i[1]
            if (isMoveable(currentY, currentX)):
                if map[y][x] + 1 > max:
                    failFlag = True
                    break
                if map[currentY][currentX] > map[y][x]:
                    continue
                map[currentY][currentX] = map[y][x] + 1
                queue.append([currentY, currentX])
    return failFlag, map


res, arrays = BFS(0, 0, arrays, K)

if not res:
    print("YES")
    for array in arrays:
        print(" ".join(map(str, array)))
else:
    print("NO")
