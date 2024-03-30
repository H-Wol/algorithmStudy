from sys import stdin

input = stdin.readline

N, new_score, P = map(int, input().split())
scores = list(map(int, input().split()))

if N == 0:
    rank = 1
else:
    if N == P and scores[-1] >= new_score:
        rank = -1
    else:
        rank = 1
        for s in scores:
            if s > new_score:
                rank += 1
                if rank > P:
                    rank = -1
                    break

print(rank)
