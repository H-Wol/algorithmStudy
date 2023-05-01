from itertools import permutations


N = int(input())

nums = [i for i in range(1, N + 1)]


num_permutations = list(permutations(nums, N))
for i in num_permutations:
    print(" ".join(map(str, i)))
