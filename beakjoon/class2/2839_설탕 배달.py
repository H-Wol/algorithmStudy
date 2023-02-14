import sys

N = int(sys.stdin.readline())


def getSugar(N):
    max_5 = N // 5
    if N % 5 == 0:
        return int(max_5)
    else:
        for i in range(max_5, -1, -1):
            if (N - (i * 5)) % 3 == 0:
                return int(i + (N - (i * 5)) // 3)
        return -1


print(getSugar(N))
4
4
