from sys import stdin
import heapq

input = stdin.readline
n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

total_moves = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    new_card = card1 + card2
    total_moves += new_card

    heapq.heappush(cards, new_card)

print(total_moves)
