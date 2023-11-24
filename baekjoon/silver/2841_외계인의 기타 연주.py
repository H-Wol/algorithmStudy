from sys import stdin

input = stdin.readline

n, p = map(int, input().split())

stacks = [[] for _ in range(7)]
count = 0

for _ in range(n):
    line, fret = map(int, input().split())

    while stacks[line] and stacks[line][-1] > fret:
        stacks[line].pop()
        count += 1

    if not stacks[line] or stacks[line][-1] < fret:
        stacks[line].append(fret)
        count += 1

print(count)
