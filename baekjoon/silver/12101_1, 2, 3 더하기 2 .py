from sys import stdin

input = stdin.readline
N, K = map(int, input().split())


def count_ways(n):
    if n == 1:
        return ["1"]
    if n == 2:
        return ["1+1", "2"]
    if n == 3:
        return ["1+1+1", "1+2", "2+1", "3"]

    ways = []
    for i in range(1, 4):
        sub_ways = count_ways(n - i)
        for sub_way in sub_ways:
            ways.append(str(i) + "+" + sub_way)

    return ways


ways = count_ways(N)

if K > len(ways):
    print(-1)
else:
    print(ways[K - 1])
