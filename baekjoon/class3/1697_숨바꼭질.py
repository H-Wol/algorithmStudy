import sys

N, K = map(int, sys.stdin.readline().split(" "))


def moveable(x):
    return x-1, x+1, x*2


def isMoveable(x, map):
    if (100_000+1 > x >= 0 and map[x] == 0):
        return True
    return False


# [visited]
field = [0 for _ in range(100_000+1)]


def BFS(x, y, map):
    cnt = 0
    if (isMoveable(x, map)):
        map[x] = 1
        queue = [x]
        tmp = []
        while (queue):
            pos = queue.pop(0)
            if pos == y:
                break
            for i in moveable(pos):
                if (isMoveable(i, map)):
                    map[i] = 1
                    tmp.append(i)
            if queue == []:
                queue = tmp
                tmp = []
                cnt += 1

    return cnt


print(BFS(N, K, field))
