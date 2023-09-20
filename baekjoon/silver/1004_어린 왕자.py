from sys import stdin

input = stdin.readline

T = int(input())

def is_inside(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_inside = is_inside(x1, y1, cx, cy, r)
        end_inside = is_inside(x2, y2, cx, cy, r)

        if start_inside != end_inside:
            count += 1

    print(count)
