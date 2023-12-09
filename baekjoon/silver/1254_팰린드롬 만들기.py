from sys import stdin
input = stdin.readline

S = input().strip()


def is_palindrome(s):
    return s == s[::-1]


for i in range(len(S)):
    if is_palindrome(S[i:]):
        print(len(S + S[:i][::-1]))
        exit()
