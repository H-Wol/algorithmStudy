import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    str = input().rstrip()
    n = int(input())
    lists = deque(eval(input().rstrip()))
    isReversed = False
    continueFlag = False

    for i in str:
        if i == "R":
            isReversed = not isReversed
        else:
            if len(lists) == 0:
                print("error")
                continueFlag = True
                break
            if isReversed:
                lists.pop()
            else:
                lists.popleft()
    if continueFlag:
        continue
    if isReversed:
        lists.reverse()
    print("[", end="")
    print(*lists, sep=",", end="")
    print("]")
