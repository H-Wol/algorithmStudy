from sys import stdin

input = stdin.readline

N, K, B = map(int, input().split())
broken_lights = set(int(input()) for _ in range(B))

min_repair = float('inf')
current_repair = sum(1 for i in range(1, K + 1) if i in broken_lights)
min_repair = min(min_repair, current_repair)
for i in range(2, N - K + 2):
    if i - 1 in broken_lights:
        current_repair -= 1
    if i + K - 1 in broken_lights:
        current_repair += 1
    min_repair = min(min_repair, current_repair)

print(min_repair)
