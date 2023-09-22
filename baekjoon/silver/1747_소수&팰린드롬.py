n = int(input())


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(s):
    return s == s[::-1]


while True:
    if is_prime(n) and is_palindrome(str(n)):
        print(n)
        break
    n += 1
