from sys import stdin

input = stdin.readline

N = int(input())

cheese = list(set(list(map(str, input().rstrip().split(" ")))))

cnt = 0

for i in cheese:
    if i.endswith("Cheese"):
        cnt += 1

if cnt >= 4:
    print("yummy")
else:
    print("sad")
