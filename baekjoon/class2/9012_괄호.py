from sys import stdin

input = stdin.readline
T = int(input())


def isVPS(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append(True)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


for _ in range(T):
    print(isVPS(input().rstrip()))
