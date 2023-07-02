import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    length, target = map(int, input().split(" "))
    queue = deque(list(map(int, input().split(" "))))
    cnt = 0
    while True:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if target == 0:
                break
        else:
            queue.append(queue.popleft())
        target -= 1
        if target < 0:
            target = len(queue) - 1
    print(cnt)
