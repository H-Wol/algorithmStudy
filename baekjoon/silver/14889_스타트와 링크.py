from itertools import combinations
from sys import stdin

input = stdin.readline


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_difference = float("inf")


def calculate_difference(team):
    total = 0
    for i in team:
        for j in team:
            total += S[i][j]
    return total


for start_team in combinations(range(N), N // 2):
    link_team = [i for i in range(N) if i not in start_team]

    start_score = calculate_difference(start_team)
    link_score = calculate_difference(link_team)

    min_difference = min(min_difference, abs(start_score - link_score))

print(min_difference)
