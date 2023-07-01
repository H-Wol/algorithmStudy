from sys import stdin

n = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))
line = [0] * n

for i in range(1, n + 1):
    count = heights[i - 1]
    for j in range(n):
        if line[j] == 0 and count == 0:
            line[j] = i
            break
        elif line[j] == 0:
            count -= 1

print(" ".join(map(str, line)))
