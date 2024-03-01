from sys import stdin

input = stdin.readline


def solve(n):
    if n % 2 == 1:
        return "SK"
    else:
        return "CY"


n = int(input())
result = solve(n)
print(result)
