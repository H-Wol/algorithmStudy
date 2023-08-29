from sys import stdin

input = stdin.readline


n = int(input())
total_moves = 2**n - 1
print(total_moves)


def hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(from_peg, to_peg)
        return

    hanoi(n - 1, from_peg, aux_peg, to_peg)
    print(from_peg, to_peg)
    hanoi(n - 1, aux_peg, to_peg, from_peg)


if n <= 20:
    hanoi(n, 1, 3, 2)
