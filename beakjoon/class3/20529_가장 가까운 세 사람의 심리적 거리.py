import sys

input = sys.stdin.readline

T = int(input())

while T:
    ans = 999999
    T -= 1
    N = int(input())
    a = list(map(str, input().split()))
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if a[i][x] != a[j][x]:
                            tmp += 1
                        if a[j][x] != a[k][x]:
                            tmp += 1
                        if a[i][x] != a[k][x]:
                            tmp += 1
                    ans = min(tmp, ans)
        print(ans)
