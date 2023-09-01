from sys import stdin

input = stdin.readline


k = int(input())
nodes = list(map(int, input().split()))

result = [[] for _ in range(k)]


def in_order_traversal(arr, depth, left, right):
    if depth == k:
        return
    middle = (left + right) // 2
    result[depth].append(arr[middle])
    in_order_traversal(arr, depth + 1, left, middle)
    in_order_traversal(arr, depth + 1, middle + 1, right)


in_order_traversal(nodes, 0, 0, len(nodes))

for level in result:
    print(*level)
