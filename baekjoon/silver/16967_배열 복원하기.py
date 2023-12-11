from sys import stdin

input = stdin.readline

N = int(input())

# 총 조각의 수 계산
total_slices = N * (N - 1) // 2

print(total_slices)
