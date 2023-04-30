N = int(input())
counts = [1, 2]
for i in range(2, N):
    counts.append((counts[i - 1] + counts[i - 2]) % 15746)

print(counts[N - 1])
