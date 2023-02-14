import sys

N = int(sys.stdin.readline())
queue = []

orders = ['pop', 'top']
orders2 = ['size', 'empty']


def order(str):
    global queue
    if str in orders:
        if queue == []:
            print(-1)
        elif str == orders[0]:
            print(queue.pop())
        else:
            print(queue[-1])
    elif str == 'size':
        print(len(queue))
    elif str == 'empty':
        print(0 if len(queue) else 1)
    else:
        queue.append(int((str.split(" ")[1])))


for i in range(N):
    order(sys.stdin.readline().rstrip())
