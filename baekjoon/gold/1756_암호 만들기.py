from sys import stdin
from itertools import combinations


def is_valid(password):
    vowels = {"a", "e", "i", "o", "u"}
    vowel_count = 0
    consonant_count = 0

    for char in password:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count >= 1 and consonant_count >= 2


def generate_passwords(l, characters):
    passwords = []
    for password in combinations(characters, l):
        if is_valid(password):
            passwords.append("".join(sorted(password)))

    return passwords


input = stdin.readline
l, c = map(int, input().split())
characters = input().split()

characters.sort()
passwords = generate_passwords(l, characters)

for password in passwords:
    print(password)
