from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split(" "))

array = deque([i for i in range(1, N+1)])
answer = []
count = 0
while len(array) > 0:
    count += 1
    count %= K
    if count:
        array.append(array.popleft())
    else:
        answer.append(array.popleft())


print(f"<{', '.join(map(str, answer))}>")
