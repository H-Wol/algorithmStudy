from sys import stdin
from collections import deque

input = stdin.readline

n, w, L = map(int, input().split())
truck_weights = list(map(int, input().split()))

time = 0
bridge = deque([0] * w)

total_weight = 0
while truck_weights:
    time += 1

    total_weight -= bridge.popleft()

    if total_weight + truck_weights[0] <= L:
        total_weight += truck_weights[0]
        bridge.append(truck_weights.pop(0))
    else:
        bridge.append(0)

print(time + w)
