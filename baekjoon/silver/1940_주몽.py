from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
materials = list(map(int, input().split()))
count = 0
materials_set = set(materials)

for material in materials:
    target = M - material
    if target in materials_set and target != material:
        count += 1

print(count // 2)
