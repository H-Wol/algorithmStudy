from sys import stdin

input = stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

max_weight = 0

for i, rope in enumerate(ropes):
    weight = rope * (len(ropes) - i)
    max_weight = max(max_weight, weight)


print(max_weight)
