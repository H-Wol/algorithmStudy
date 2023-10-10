import sys
from sys import stdin
from itertools import combinations

input = stdin.readline


def calculate_team_difference(team, ability):
    total = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                total += ability[team[i]][team[j]]
    return total


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

min_difference = sys.maxsize

for i in range(1, N // 2 + 1):
    team_combinations = combinations(range(N), i)
    for team1 in team_combinations:
        team1 = set(team1)
        team2 = set(range(N)) - team1
        team1 = list(team1)
        team2 = list(team2)

        difference = abs(calculate_team_difference(team1, ability) - calculate_team_difference(team2, ability))
        min_difference = min(min_difference, difference)

print(min_difference)
