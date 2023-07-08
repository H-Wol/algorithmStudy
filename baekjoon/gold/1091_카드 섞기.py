from sys import stdin

input = stdin.readline


def check_sequence(n, p, S):
    cards = [0, 1, 2] * int((n / 3))
    originCards = cards[:]
    count = 0

    while cards != p:
        count += 1
        new_cards = [0] * n
        for i in range(n):
            new_cards[i] = cards[S[i]]

        cards = new_cards[:]

        if cards == originCards:
            return -1

    return count


N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

result = check_sequence(N, P, S)
print(result)
