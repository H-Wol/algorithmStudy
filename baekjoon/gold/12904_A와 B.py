from sys import stdin

input = stdin.readline


def can_transform(s, t):
    while len(s) < len(t):
        if t[-1] == "A":
            t = t[:-1]
        else:
            t = t[:-1][::-1]

    return s == t


s = input().strip()
t = input().strip()

if can_transform(s, t):
    print(1)
else:
    print(0)
