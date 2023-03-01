import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_heap = []
    min_heap = []
    length = 0
    available = {}
    k = int(input())
    for seq in range(k):
        operation, num = map(str, input().rstrip().split(" "))
        if operation == "I":
            length += 1
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, (-int(num), int(num)))
            available[int(num)] = available.get(int(num), 0) + 1
        else:
            if length == 0:
                max_heap = []
                min_heap = []
                continue
            length -= 1
            target = 0
            if int(num) > 0:
                target = heapq.heappop(max_heap)[1]
                while available.get(target, 0) == 0:
                    target = heapq.heappop(max_heap)[1]
            else:
                target = heapq.heappop(min_heap)
                while available.get(target, 0) == 0:
                    target = heapq.heappop(min_heap)
            available[target] = available.get(target, 0) - 1

    if length:
        min, max = 0, 0
        while min_heap:
            x = heapq.heappop(min_heap)
            if available.get(x, 0) > 0:
                min = x
                break
        while max_heap:
            y = heapq.heappop(max_heap)[1]
            if available.get(y, 0) > 0:
                max = y
                break
        print(max, min)
    else:
        print("EMPTY")
