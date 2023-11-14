from sys import stdin


input = stdin.readline


def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return is_prime


def count_prime_factors(num):
    count = 0
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            count += 1
            num //= i
    if num > 1:
        count += 1
    return count


A, B = map(int, input().split())
primes = prime_sieve(B)
count = 0

for i in range(A, B + 1):
    divisors_count = count_prime_factors(i)
    if primes[divisors_count]:
        count += 1

print(count)
