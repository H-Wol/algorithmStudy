from sys import stdin

input = stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]

for num in sorted(numbers, reverse=True):
    print(num)
