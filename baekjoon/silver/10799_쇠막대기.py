from sys import stdin

input = stdin.readline

s = input().strip()

stack = []
count = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        if stack[-1] + 1 == i:
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
