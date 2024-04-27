from collections import deque
from sys import stdin

input = stdin.readline


N = int(input())
commands = [input().readline().strip() for _ in range(N)]
dq = deque()

for command in commands:
    if command[0] == "1":
        num = int(command.split()[1])
        dq.appendleft(num)
    elif command[0] == "2":
        num = int(command.split()[1])
        dq.append(num)
    elif command == "3":
        print(dq.popleft() if dq else -1)
    elif command == "4":
        print(dq.pop() if dq else -1)
    elif command == "5":
        print(len(dq))
    elif command == "6":
        print(0 if dq else 1)
    elif command == "7":
        print(dq[0] if dq else -1)
    elif command == "8":
        print(dq[-1] if dq else -1)
