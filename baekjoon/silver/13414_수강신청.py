from sys import stdin

input = stdin.readline

K, L = map(int, input().split())
reqs = {}
for i in range(L):
    reqs[input().rstrip()] = i
reqs = sorted(reqs.items(), key=lambda item: item[1])

if len(reqs) > K:
    reqs = reqs[:K]
for req in reqs:
    print(req[0])
