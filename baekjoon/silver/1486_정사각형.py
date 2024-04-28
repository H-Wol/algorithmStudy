from sys import stdin
from collections import deque

input = stdin.readline


def check_square(points):
    distances = set()
    for i in range(4):
        for j in range(i + 1, 4):
            distances.add(
                (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            )
    return len(distances) == 2 and 2 * min(distances) == max(distances)


T = int(input().strip())

for _ in range(T):
    points = [list(map(int, input().strip().split())) for _ in range(4)]
    print(1 if check_square(points) else 0)
