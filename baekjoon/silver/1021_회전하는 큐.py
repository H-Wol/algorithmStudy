import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split(" "))

queue = deque([i for i in range(1, N + 1)])

cnt = 0

poses = map(int, input().split(" "))

for pos in poses:
    try:
        idx = queue.index(pos, 0, (len(queue) // 2) + 1)
        direction = -1
    except Exception as e:
        direction = 1
    while queue[0] != pos:
        cnt += 1
        queue.rotate(direction)
    queue.popleft()
print(cnt)
