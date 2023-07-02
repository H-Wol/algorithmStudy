import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def add(num: int, target):
    res = [num+1, num+2, num+3]
    if target in res:
        return 1, [i for i in res if i != target]
    return 0, res


for _ in range(T):
    n = int(input())
    count = 0
    left = deque([0])
    while min(left) < n:
        cnt, res = add(left.popleft(), n)
        count += cnt
        left.extend(res)
    print(count)
