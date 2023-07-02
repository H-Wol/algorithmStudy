from sys import stdin, maxsize
from itertools import combinations

input = stdin.readline

N, M = map(int, input().split())

chicks = []
houses = []
for i in range(1, N + 1):
    line = list(map(int, input().split()))
    for j in range(1, N + 1):
        if line[j - 1] == 1:
            houses.append([i, j])
        elif line[j - 1] == 2:
            chicks.append([i, j])


def get_distance(house, chickens: list):
    return min([abs(cur[0] - house[0]) + abs(cur[1] - house[1]) for cur in chickens])


if len(chicks) == M:
    print(sum([get_distance(house, chicks) for house in houses]))
    exit()

min_len = maxsize

chicks_combinations = list(combinations(chicks, M))

for comb in chicks_combinations:
    cur_len = 0
    flag = True
    for house in houses:
        cur_len += get_distance(house, comb)
        if cur_len > min_len:
            flag = False
            break
    if flag and cur_len < min_len:
        min_len = cur_len
print(min_len)
