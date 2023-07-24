from collections import deque
from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
durability = list(map(int, input().split()))

conveyor = deque(durability[: 2 * n])
robots = deque([False] * n)

level = 1

while True:
    conveyor.rotate(1)
    robots.rotate(1)
    robots[n - 1] = False

    for i in range(n - 2, -1, -1):
        if robots[i] and not robots[i + 1] and conveyor[i + 1] >= 1:
            robots[i + 1] = True
            robots[i] = False
            conveyor[i + 1] -= 1

    robots[n - 1] = False

    if not robots[0] and conveyor[0] >= 1:
        robots[0] = True
        conveyor[0] -= 1

    zero_count = conveyor.count(0)
    if zero_count >= k:
        break

    level += 1

print(level)
