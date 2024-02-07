A, B = input().split()
min_difference = float('inf')

for i in range(len(B) - len(A) + 1):
    difference = sum(c1 != c2 for c1, c2 in zip(A, B[i:]))
    min_difference = min(min_difference, difference)


print(min_difference)
