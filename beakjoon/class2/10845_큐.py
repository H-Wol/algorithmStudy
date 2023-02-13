import sys

N = int(sys.stdin.readline())
queue = []

orders = ['pop', 'front', 'back']
orders2 = ['size', 'empty']


def order(str):
    global queue
    if str in orders:
        if queue == []:
            print(-1)
        elif str == orders[0]:
            print(queue.pop())
        elif str == orders[1]:
            print(queue[-1])
        else:
            print(queue[0])
    elif str == 'size':
        print(len(queue))
    elif str == 'empty':
        print(0 if len(queue) else 1)
    else:
        tmp = [int((str.split(" ")[1]))]
        tmp.extend(queue)
        queue = tmp


for i in range(N):
    order(sys.stdin.readline().rstrip())
