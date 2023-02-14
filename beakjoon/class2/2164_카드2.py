import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque([i for i in range(1, N+1)])


if len(cards) == 1:
    print(cards[0])
else:
    while len(cards) != 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])
