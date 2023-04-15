from fractions import Fraction

factorial_dict = {}

n, m = map(int, input().split(" "))


def factorial(i):
    if i < 2:
        return 1
    if i not in factorial_dict:
        factorial_dict[i] = i * factorial(i - 1)
    return factorial_dict[i]


print(int(Fraction(factorial(n), (factorial(m) * factorial(n - m)))))
