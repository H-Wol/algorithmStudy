from sys import stdin
from itertools import combinations

input = stdin.readline


while True:
    input_data = list(map(int, input().split()))

    if input_data[0] == 0:
        break

    k, numbers = input_data[0], input_data[1:]

    combinations_list = list(combinations(numbers, 6))

    for combination in combinations_list:
        print(" ".join(map(str, combination)))
    print()
