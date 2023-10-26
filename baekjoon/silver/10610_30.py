from sys import stdin

input = stdin.readline

num_str = input().strip()
digits = [int(digit) for digit in num_str]

total = sum(digits)

digits.sort(reverse=True)

if total % 3 == 0 and digits[-1] == 0:
    print("".join(map(str, digits)))
else:
    print("-1")
