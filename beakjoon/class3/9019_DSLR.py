import sys
from collections import deque
input = sys.stdin.readline


def D(n):
    return (n*2) % 10000


def S(n):
    return n-1 if n > 0 else 9999


def L(n):
    return (n % 1000)*10 + n // 1000


def R(n):
    return (n % 10)*1000 + n // 10


def DSLR(n):
    return [D(n), "D"], [S(n), "S"], [L(n), "L"], [R(n), "R"]


def BFS(A, B, map):
    map[A][0] = True
    queue = deque([A])
    while (queue):
        cur = queue.popleft()
        for i in DSLR(cur):
            if i[0] == B:
                print(map[cur][1] + i[1])
                return
            if map[i[0]][0] == False:
                map[i[0]][0] = True
                map[i[0]][1] = map[cur][1] + i[1]
                queue.append(i[0])


T = int(input())
for _ in range(T):
    field = [[False, ""] for _ in range(100_00)]
    A, B = map(int, input().split(" "))
    BFS(A, B, field)
