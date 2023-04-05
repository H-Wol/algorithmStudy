N = int(input())
counts = [1, 3]
for i in range(2, N):
    counts.append((counts[i - 1] + counts[i - 2] * 2) % 10007)

print(counts[N - 1])
