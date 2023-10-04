from sys import stdin

input = stdin.readline
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

max_sum = sum(temperatures[:K])
current_sum = max_sum

for i in range(K, N):
    current_sum = current_sum - temperatures[i - K] + temperatures[i]
    max_sum = max(max_sum, current_sum)

print(max_sum)
