from sys import stdin

input = stdin.readline

N = int(input())
queue = []

orders = [2, 5]


def order(str):
    global queue
    if str[0] in orders:
        if queue == []:
            print(-1)
        elif str[0] == orders[0]:
            print(queue.pop())
        else:
            print(queue[-1])
    elif str[0] == 3:
        print(len(queue))
    elif str[0] == 4:
        print(0 if len(queue) else 1)
    else:
        queue.append(str[1])


for i in range(N):
    order(list(map(int, input().rsplit())))
