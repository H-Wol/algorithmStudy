import sys
from collections import deque
N = int(sys.stdin.readline())
deck = deque([])

frontOrBack = ['front', 'back']


def order(str):
    global deck
    if str in frontOrBack:
        if len(deck) == 0:
            print(-1)
        elif str == frontOrBack[0]:
            print(deck[0])
        else:
            print(deck[-1])
    elif str == 'size':
        print(len(deck))
    elif str == 'empty':
        print(0 if len(deck) else 1)
    else:
        orders = str.split(" ")
        if "push" in orders[0]:
            if "front" in orders[0]:
                deck.appendleft(int(orders[1]))
            else:
                deck.append(int(orders[1]))
        else:
            if len(deck) == 0:
                print(-1)
            elif "front" in orders[0]:
                print(deck.popleft())
            else:
                print(deck.pop())


for i in range(N):
    order(sys.stdin.readline().rstrip())
