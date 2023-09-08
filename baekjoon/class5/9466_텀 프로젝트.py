from sys import stdin
import sys

sys.setrecursionlimit(111111)

input = stdin.readline

T = int(input())
team_cnt = 0


def dfs(peek: int, peeks: list, visited: list):
    global team_cnt
    cur_team_list.append(peek)
    visited[peek] = True
    if not visited[peeks[peek]]:
        return dfs(peeks[peek], peeks, visited)
    if peeks[peek] in cur_team_list:
        team_cnt += len(cur_team_list) - cur_team_list.index(peeks[peek])
        return


for _ in range(T):
    n = int(input())
    visited = [False for _ in range(n)]
    peeks = list(map(int, input().rsplit()))
    peeks.insert(0, 0)
    visited.insert(0, True)
    team_cnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        cur_team_list = []
        dfs(i, peeks, visited)
    print(n - team_cnt)
