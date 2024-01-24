from sys import stdin
import re

input = stdin.readline

T = int(input())


def is_contact(sequence):
    pattern = re.compile('(100+1+|01)+')
    match = pattern.fullmatch(sequence)
    return match is not None


for _ in range(T):
    sequence = input().rstrip()
    result = "YES" if is_contact(sequence) else "NO"
    print(result)
