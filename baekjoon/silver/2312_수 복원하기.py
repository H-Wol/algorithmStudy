from sys import stdin

input = stdin.readline


def prime_factorization(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors


def restore_number(n):
    factors = prime_factorization(n)
    result = []
    for factor, count in factors.items():
        result.append((factor, count))
    return result


T = int(input())
for _ in range(T):
    N = int(input())
    factors = restore_number(N)
    for factor, count in factors:
        print(f"{factor} {count}")
