from sys import stdin

input = stdin.readline


def find_divisible_number(n):
    current = 1
    count = 1

    while True:
        if current % n == 0:
            return count
        current = (current * 10 + 1) % n
        count += 1


while True:
    try:
        n = int(input())
        result = find_divisible_number(n)
        print(result)
    except:
        break
