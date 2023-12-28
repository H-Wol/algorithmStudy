from sys import stdin

input = stdin.readline


A_size, B_size = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))


def symmetric_difference(set_a, set_b):
    diff_a_b = set_a - set_b
    diff_b_a = set_b - set_a
    return diff_a_b.union(diff_b_a)


result_set = symmetric_difference(set_a, set_b)
result = len(result_set)

print(result)
