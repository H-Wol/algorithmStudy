from sys import stdin

input = stdin.readline
n = int(input())
choo = list(map(int, input().split()))

possible = set()


def possible_weights(choo, idx, current_weight, possible):
    if idx == len(choo):
        if current_weight > 0:
            possible.add(current_weight)
        return

    possible_weights(choo, idx + 1, current_weight, possible)

    possible_weights(choo, idx + 1, current_weight + choo[idx], possible)

    possible_weights(choo, idx + 1, abs(current_weight - choo[idx]), possible)


possible_weights(choo, 0, 0, possible)

total_weight = sum(choo)
print(total_weight - len(possible))
