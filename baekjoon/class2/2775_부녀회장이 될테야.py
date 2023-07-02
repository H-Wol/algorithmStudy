import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    sum = 0
    f0 = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            f0[j] += f0[j-1]
    print(f0[-1])
