from sys import stdin

input = stdin.readline


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


def ccw(x1, y1, x2, y2, x3, y3):
    result = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0


result = ccw(x1, y1, x2, y2, x3, y3)
print(result)
