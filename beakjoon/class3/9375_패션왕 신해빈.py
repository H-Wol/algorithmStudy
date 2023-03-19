import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = defaultdict(int)
    for _ in range(N):
        name, kind = map(str, input().rstrip().split(" "))
        clothes[kind] += 1

    result = 1
    for count in clothes.values():
        result *= count + 1
    print(result - 1)
