import sys
input = sys.stdin.readline

N = int(input())
people = []
ranks = []
for _ in range(N):
    people.append(list(map(int, input().split(" "))))

for i in range(N):
    target = people[i]
    rank = 1
    for j in range(N):
        if j == i:
            continue
        if people[j][0] > target[0] and people[j][1] > target[1]:
            rank += 1
    ranks.append(rank)

print(' '.join(map(str, ranks)))
