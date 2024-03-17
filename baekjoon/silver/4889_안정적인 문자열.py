from sys import stdin

input = stdin.readline


def min_operations(s):
    stack = []
    count = 0

    for c in s:
        if c == '{':
            stack.append(c)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append('{')
                count += 1

    count += len(stack) // 2
    return count


case = 1
while True:
    s = input().rstrip()
    if '-' in s:
        break
    result = min_operations(s)
    print(f"{case}. {result}")
    case += 1
