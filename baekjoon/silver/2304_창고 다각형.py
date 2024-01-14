from sys import stdin

input = stdin.readline

n = int(input())
pillars = [0] * 1001

for _ in range(n):
    position, height = map(int, input().split())
    pillars[position] = height

max_height = max(pillars)
max_height_index = pillars.index(max_height)

left_max = 0
current_height = 0
area = 0

for i in range(max_height_index + 1):
    if pillars[i] > current_height:
        current_height = pillars[i]
    area += current_height

right_max = 0
current_height = 0
for i in range(len(pillars) - 1, max_height_index, -1):
    if pillars[i] > current_height:
        current_height = pillars[i]
    area += current_height
print(area)
