from sys import stdin

input = stdin.readline

N = int(input().strip())
heights = []

for _ in range(N):
    height = int(input().strip())
    heights.append(height)

stack = []
count = 0
for height in heights:
    while stack and stack[-1] <= height:
        stack.pop()
    count += len(stack)
    stack.append(height)
print(count)
