from sys import stdin

input = stdin.readline


def count_students(colors, num_students):
    low = 1
    high = max(colors)

    while low <= high:
        mid = (low + high) // 2
        count = 0

        for color in colors:
            count += (color + mid - 1) // mid

        if count <= num_students:
            high = mid - 1
        else:
            low = mid + 1

    return low


n, m = map(int, input().split())
colors = []

for _ in range(m):
    colors.append(int(input()))

print(count_students(colors, n))
