from sys import stdin


input = stdin.readline


N = int(input())

strings = []
dicts = {input().rstrip(): 1}
for _ in range(1, N):
    flag = True
    str = input().rstrip()
    for i in range(len(str)):
        s = str[i:] + str[0:i]
        if dicts.get(s, 0) != 0:
            dicts[s] = dicts[s] + 1
            flag = False
            break
    if flag:
        dicts[str] = 1

print(len(dicts))
