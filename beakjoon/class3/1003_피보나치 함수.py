import sys
input = sys.stdin.readline

N = int(input())

fibRes = [[1, 0], [0, 1]]


def addFunc(x, y): return (x[0]+y[0], x[1]+y[1])


for _ in range(N):
    target = int(input())
    while len(fibRes) < target+1:
        fibRes.append(addFunc(fibRes[-2], fibRes[-1]))
    print(" ".join(map(str, fibRes[target])))
