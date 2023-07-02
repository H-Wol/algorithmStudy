import sys


A, B = map(int, sys.stdin.readline().split(" "))

from collections import deque

queue = deque([A])   
cnt = {
    A : 1
}

def function(num):
    return num*2, int(f"{num}1")

while queue:
    cur = queue.popleft()
    for i in function(cur):
        if i == B:
            print(cnt.get(cur)+1)
            exit()
        elif i > B:
            continue
        else:
            queue.append(i)
            cnt[i] = cnt.get(cur)+1
print(-1)
