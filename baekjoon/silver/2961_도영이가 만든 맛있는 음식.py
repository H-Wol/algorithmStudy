from sys import stdin
from itertools import combinations

input = stdin.readline
n = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]
min_taste = float('inf')


def calculate_taste(combo):
    sourness = 1
    bitterness = 0

    for i in combo:
        sourness *= ingredients[i][0]
        bitterness += ingredients[i][1]

    return abs(sourness - bitterness)


for r in range(1, len(ingredients) + 1):
    for combo in combinations(range(len(ingredients)), r):
        min_taste = min(min_taste, calculate_taste(combo))

print(min_taste)
