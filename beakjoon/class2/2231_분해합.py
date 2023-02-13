N = int(input())


def getDecomposition(N):
    for i in range(N):
        if (i + sum(int(x) for x in list(str(i)))) == N:
            print(i)
            return 0
    print(0)


getDecomposition(N)
