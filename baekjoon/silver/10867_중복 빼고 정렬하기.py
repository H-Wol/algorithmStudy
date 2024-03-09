from sys import stdin

input = stdin.readline

N = int(input())
numbers = set(list(map(int, input().split())))

result = sorted(list(numbers))
print(*result)
