import sys

N = int(sys.stdin.readline())

results = [N]
cnt = 0


def calc(n):
    tmp = []
    if (n % 2) == 0:
        tmp.append(n//2)
    if (n % 3) == 0:
        tmp.append(n//3)
    tmp.append(n-1)
    return tmp


while True:
    if 1 in results:
        break
    cnt += 1
    tmp = []
    for result in results:
        tmp.extend(res := calc(result))
        if 1 in res:
            tmp = res
            break
    results = tmp
print(cnt)
