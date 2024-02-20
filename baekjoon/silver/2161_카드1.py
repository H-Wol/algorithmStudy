from collections import deque
from sys import stdin

input = stdin.readline


def simulate_card_deck(N):
    deck = deque(range(1, N + 1))
    discarded_cards = []

    while len(deck) > 1:
        discarded_cards.append(deck.popleft())
        deck.append(deck.popleft())
    discarded_cards.append(deck[0])

    return discarded_cards


N = int(input())
result = simulate_card_deck(N)

print(*result)
