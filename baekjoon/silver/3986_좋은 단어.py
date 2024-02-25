from sys import stdin

input = stdin.readline

N = int(input())
count = 0

for _ in range(N):
    word = input().strip()
    stack = []

    for char in word:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    if not stack:
        count += 1

print(count)
