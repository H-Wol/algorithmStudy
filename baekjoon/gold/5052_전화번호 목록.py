from sys import stdin

input = stdin.readline
t = int(input().strip())


def is_consistent(phone_numbers):
    phone_numbers.sort()
    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i] == phone_numbers[i + 1][:len(phone_numbers[i])]:
            return "NO"
    return "YES"


for _ in range(t):
    n = int(input().strip())
    phone_numbers = [input().strip() for _ in range(n)]
    result = is_consistent(phone_numbers)
    print(result)
