from sys import stdin

input = stdin.readline


N, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
numbers
