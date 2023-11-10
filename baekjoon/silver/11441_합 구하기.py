from sys import stdin

input = stdin.readline

N = int(input())


input_list = list(map(int, input().rsplit()))
sum_list = [0] * (N+1)
for idx, val in enumerate(input_list):
    sum_list[idx+1] = sum_list[idx] + val

M = int(input())

for _ in range(M):
    i, j = map(int, input().rsplit())
    print(sum_list[j] - sum_list[i-1])
