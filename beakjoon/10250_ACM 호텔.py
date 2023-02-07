times = int(input())


def findRoom(H, W, N):
    n = 0
    for w in range(1, W+1):
        for h in range(1, H+1):
            n += 1
            if n == N:
                print(str(h)+str(w).zfill(2))
                return 0


for time in range(times):
    H, W, N = map(int, input().split())
    findRoom(H, W, N)
