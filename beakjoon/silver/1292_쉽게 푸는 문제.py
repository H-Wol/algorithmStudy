import sys

input = sys.stdin.readline

A, B = map(int, input().split(" "))

cnt = 0
lists = []
while len(lists) < B:
    cnt += 1
    for _ in range(cnt):
        lists.append(cnt)
print(sum(lists[A - 1 : B]))
