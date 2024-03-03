from sys import stdin

input = stdin.readline


def count_trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    result = count_trailing_zeros(N)
    print(result)
