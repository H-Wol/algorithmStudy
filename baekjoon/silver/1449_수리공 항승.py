from sys import stdin

input = stdin.readline

n, l = map(int, input().split())
leak_points = list(map(int, input().split()))

leak_points.sort()
tape_count = 0
start = leak_points[0]

for point in leak_points:
    if point - start > l - 1:
        tape_count += 1
        start = point

print(tape_count + 1)
