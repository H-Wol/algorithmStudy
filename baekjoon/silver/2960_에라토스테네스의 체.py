from sys import stdin

input = stdin.readline


def find_kth_prime(n, k):
    is_prime = [False, False] + [True] * (n - 1)
    count = 0

    for number in range(2, n + 1):
        if is_prime[number]:
            for multiple in range(number, n + 1, number):
                if is_prime[multiple]:
                    is_prime[multiple] = False
                    count += 1
                    if count == k:
                        return multiple


n, k = map(int, input().split())

result = find_kth_prime(n, k)
print(result)
