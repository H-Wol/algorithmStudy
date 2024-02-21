from sys import stdin

input = stdin.readline


def generate_sequence(A, P):
    sequence = [A]
    while True:
        next_number = sum(int(digit) ** P for digit in str(sequence[-1]))
        if next_number in sequence:
            break
        sequence.append(next_number)
    return sequence, next_number


A, P = map(int, input().split())
result_sequence, last_number = generate_sequence(A, P)

index_of_repeat = result_sequence.index(last_number)
print(index_of_repeat)
