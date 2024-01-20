from sys import stdin

input = stdin.readline
number = int(input().strip())
digits = [int(digit) for digit in str(number)]
sorted_digits = sorted(digits, reverse=True)
sorted_number = int(''.join(map(str, sorted_digits)))
print(sorted_number)