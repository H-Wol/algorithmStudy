from sys import stdin
from collections import defaultdict

input = stdin.readline
dancing_people = defaultdict(int)
dancing_people["ChongChong"] = 1
dancing_people_cnt = 1
N = int(input())

for _ in range(N):
    a, b = map(str, input().rsplit())
    if dancing_people[a] or dancing_people[b]:
        dancing_people_cnt += 2 - (dancing_people[a] + dancing_people[b])
        dancing_people[a], dancing_people[b] = 1, 1
print(dancing_people_cnt)
