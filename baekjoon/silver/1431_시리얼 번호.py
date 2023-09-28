from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
serials = [input().strip() for _ in range(n)]


def get_serial_key_value(serial_key):
    value = 0
    for char in serial_key:
        if char.isdigit():
            value += int(char)
    return value


def serial_key_sort(serials):
    serials.sort(key=lambda x: (len(x), get_serial_key_value(x), x))
    return serials


sorted_serials = serial_key_sort(serials)

for serial in sorted_serials:
    print(serial)
