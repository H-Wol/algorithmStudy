from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    sum_of_two = cards[0] + cards[1]
    cards[0] = sum_of_two
    cards[1] = sum_of_two

print(sum(cards))
