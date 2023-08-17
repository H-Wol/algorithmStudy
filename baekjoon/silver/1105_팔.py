from sys import stdin

input = stdin.readline

l, r = map(str, input().split())

if len(l) != len(r):
    print(0)
else:
    count = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == "8":
                count += 1
        else:
            break

    print(count)
