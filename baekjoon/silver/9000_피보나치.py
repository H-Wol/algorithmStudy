from sys import stdin

input = stdin.readline


def fibonacci_sequence(limit):
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def find_representations(n, sequence):
    representations = []
    current_sum = 0

    for i in range(len(sequence) - 1, 0, -1):
        if current_sum + sequence[i] <= n:
            representations.append(sequence[i])
            current_sum += sequence[i]
    representations.sort()
    return representations


T = int(input())

for _ in range(T):
    n = int(input())
    fibonacci_seq = fibonacci_sequence(n)
    result = find_representations(n, fibonacci_seq)

    print(" ".join(map(str, result)))
