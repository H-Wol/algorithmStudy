from sys import stdin

input = stdin.readline


def max_triangle_side(sides):
    sides.sort(reverse=True)

    for i in range(len(sides) - 2):
        if sides[i] < sides[i + 1] + sides[i + 2]:
            return sides[i] + sides[i + 1] + sides[i + 2]

    return -1  # 삼각형을 만들 수 없는 경우


N = int(input())
sides = [int(input()) for _ in range(N)]

result = max_triangle_side(sides)
print(result)
