from sys import stdin

input = stdin.readline
import math
from functools import reduce

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort()

differences = [numbers[i] - numbers[i - 1] for i in range(1, N)]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_gcd_of_list(arr):
    return reduce(gcd, arr)


gcd_value = find_gcd_of_list(differences)

divisors = set()
for i in range(1, int(math.sqrt(gcd_value)) + 1):
    if gcd_value % i == 0:
        divisors.add(i)
        divisors.add(gcd_value // i)

result = sorted([divisor for divisor in divisors if divisor > 1])
print(" ".join(map(str, result)))
