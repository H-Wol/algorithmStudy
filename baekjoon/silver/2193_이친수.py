N = int(input())

bins = [1, 1]

while len(bins) < N:
    bins.append(bins[-1] + bins[-2])
print(bins[N - 1])
