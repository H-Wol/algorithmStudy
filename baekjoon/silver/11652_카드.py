from sys import stdin
from collections import Counter

input = stdin.readline


N = int(input())
cards = [int(input()) for _ in range(N)]

card_counts = Counter(cards)
most_common_card = max(card_counts, key=lambda x: (card_counts[x], -x))

print(most_common_card)
