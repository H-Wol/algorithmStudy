from sys import stdin

input = stdin.readline

n, m = map(int, input().split())


def count_factorial_prime(n, prime):
    count = 0
    divisor = prime

    while n // divisor > 0:
        count += n // divisor
        divisor *= prime

    return count


count_2 = count_factorial_prime(
    n, 2) - count_factorial_prime(n-m, 2) - count_factorial_prime(m, 2)
count_5 = count_factorial_prime(
    n, 5) - count_factorial_prime(n-m, 5) - count_factorial_prime(m, 5)

print(min(count_2, count_5))
