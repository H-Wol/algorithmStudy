from sys import stdin

input = stdin.readline

T = int(input())


def is_pseudo_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def solution(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if is_pseudo_palindrome(s, left + 1, right) or is_pseudo_palindrome(s, left, right - 1):
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 0


for _ in range(T):
    s = input().rstrip()
    result = solution(s)
    print(result)
