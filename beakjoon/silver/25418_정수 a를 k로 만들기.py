import sys
from collections import deque
input = sys.stdin.readline

A, K = map(int, input().split(" "))

def func(num):
    return [num+1, num*2]

visited = {A :0}
queue = deque([A])
while queue:
    cur = queue.popleft()
    for i in func(cur):
        if i > K:
            continue
        if i == K:
            print(visited.get(cur) +1)
            exit()
            
        if visited.get(i,-1) == -1:
            visited[i] = visited.get(cur) +1
            queue.append(i)
            

