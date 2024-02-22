from sys import stdin

input = stdin.readline
N = int(input())
ring_sizes = list(map(int, input().split()))

first_ring = ring_sizes[0]
other_rings = ring_sizes[1:]


def find_ratio(first_ring, other_rings):
    ratios = []
    for ring in other_rings:
        gcd = find_gcd(first_ring, ring)
        ratio = (first_ring // gcd, ring // gcd)
        ratios.append(ratio)
    return ratios


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


result_ratios = find_ratio(first_ring, other_rings)

for ratio in result_ratios:
    print(f"{ratio[0]}/{ratio[1]}")
