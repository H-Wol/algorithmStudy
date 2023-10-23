from sys import stdin

input = stdin.readline

N = int(input())  #
requests = list(map(int, input().split()))
total_budget = int(input())


left, right = 0, max(requests)
result = 0

while left <= right:
    mid = (left + right) // 2
    allocated_budget = sum(min(request, mid) for request in requests)

    if allocated_budget <= total_budget:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
