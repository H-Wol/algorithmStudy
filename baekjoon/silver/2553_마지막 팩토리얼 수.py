import sys

N = int(sys.stdin.readline())

answer = 1

for i in range(1, N + 1):
    answer *= i

answer = str(answer)[::-1]
for i in range(len(answer)):
    if answer[i] != "0":
        print(answer[i])
        break
