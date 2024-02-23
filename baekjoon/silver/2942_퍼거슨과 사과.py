from sys import stdin

input = stdin.readline
M, N = map(int, input().split())


def find_divisors(gcd):
    divisors = set()

    for i in range(1, int(gcd**0.5) + 1):
        if gcd % i == 0:
            divisors.add(i)
            divisors.add(gcd // i)

    return divisors


def find_gcd(M, N):
    while N:
        M, N = N, M % N
    return M


gcd = find_gcd(M, N)
divisors = find_divisors(gcd)

for divisor in sorted(divisors):
    print(divisor, M // divisor, N // divisor)
