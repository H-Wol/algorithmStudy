k = int(input())
n = 15000000
primes = [True] * (n + 1)
primes[0] = primes[1] = False

for i in range(2, int(n**0.5) + 1):
    if primes[i]:
        for j in range(i * i, n + 1, i):
            primes[j] = False

print([x for x in range(2, n + 1) if primes[x]][k-1])
