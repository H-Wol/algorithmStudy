from sys import stdin
input = stdin.readline
x = int(input())

n = 1
while x > n:
    x -= n
    n += 1

if n % 2 == 0:
    numerator = x
    denominator = n - x + 1
else:
    numerator = n - x + 1
    denominator = x

print(f"{numerator}/{denominator}")
