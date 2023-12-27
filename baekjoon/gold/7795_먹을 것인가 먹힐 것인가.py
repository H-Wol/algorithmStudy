from sys import stdin

input = stdin.readline


def count_pairs(A, B):
    count = 0
    b_index = 0

    for a in A:
        while b_index < len(B) and B[b_index] < a:
            b_index += 1

        count += b_index

    return count


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    result = count_pairs(A, B)
    print(result)
