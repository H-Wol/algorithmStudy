from sys import stdin

input = stdin.readline


limit = 1000000
primes = [True] * (limit + 1)
primes[0], primes[1] = False, False

for i in range(2, int(limit**0.5) + 1):
    if primes[i]:
        for j in range(i * i, limit + 1, i):
            primes[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
