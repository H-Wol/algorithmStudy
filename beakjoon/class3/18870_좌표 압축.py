import sys
input = sys.stdin.readline


N = int(input())
origin_lists = list(map(int, input().split(" ")))
lists = sorted(list(set(origin_lists)))

dicts = {k: v for v, k in enumerate(lists)}

answer = [dicts.get(i) for i in origin_lists]

print(" ".join(map(str, answer)))
