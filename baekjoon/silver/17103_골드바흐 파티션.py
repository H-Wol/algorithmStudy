from sys import stdin

input = stdin.readline

t = int(input().strip())
nums = [int(input().strip()) for _ in range(t)]


def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    return is_prime


def goldbach_partition_count(nums, is_prime):
    counts = [0] * (max(nums) + 1)

    for num in nums:
        count = 0
        for i in range(2, num // 2 + 1):
            if is_prime[i] and is_prime[num - i]:
                count += 1
        counts[num] = count

    return counts


max_num = max(nums)

is_prime = sieve_of_eratosthenes(max_num)
counts = goldbach_partition_count(nums, is_prime)

for num in nums:
    print(counts[num])
