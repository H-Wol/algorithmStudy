from itertools import permutations
from sys import stdin

input = stdin.readline


def calculate_cost(order, graph, N):
    cost = 0
    for i in range(N - 1):
        if graph[order[i]][order[i + 1]] == 0:
            return float('inf')  # 경로가 없는 경우
        cost += graph[order[i]][order[i + 1]]
    if graph[order[-1]][order[0]] == 0:
        return float('inf')  # 경로가 없는 경우
    cost += graph[order[-1]][order[0]]
    return cost


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

orders = list(permutations(range(N)))
min_cost = float('inf')

for order in orders:
    cost = calculate_cost(order, graph, N)
    min_cost = min(min_cost, cost)

print(min_cost)
