import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
broken = []
if M > 0:
    broken = list(map(int, input().split(" ")))
else:
    input()

min_cnt = abs(N - 100)

max_channel = N + min_cnt
min_channel = N - min_cnt
if min_channel < 0:
    min_channel = 0
if len(broken) != 10:
    for i in range(min_channel, max_channel, 1):
        flag = True
        for num in set(map(int, str(i))):
            if int(num) in broken:
                flag = False
                break
        if flag:
            if (res := (abs(N - i) + len(str(i)))) < min_cnt:
                min_cnt = res
print(min_cnt)
