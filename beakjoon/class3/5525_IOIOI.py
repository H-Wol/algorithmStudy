import sys
input = sys.stdin.readline

N = int(input())

S = int(input())
str = input().rstrip()


target = "IOI"

cnt = 0
cur = 0
answer = 0
while cur < (S - 1):
    if str[cur:cur+3] == target:
        cnt += 1
        cur += 2
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        cur += 1
        cnt = 0


print(answer)
