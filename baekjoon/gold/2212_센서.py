from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

distances = [sensors[i + 1] - sensors[i] for i in range(N - 1)]
distances.sort(reverse=True)

result = sum(distances[K - 1:])

print(result)
