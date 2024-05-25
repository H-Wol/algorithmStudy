from sys import stdin

input = stdin.readline


N, K = map(int, input().split())
heights = list(map(int, input().split()))


heights.sort()

differences = []
for i in range(1, N):
    differences.append(heights[i] - heights[i - 1])

differences.sort(reverse=True)

min_cost = sum(differences[K - 1 :])

print(min_cost)
