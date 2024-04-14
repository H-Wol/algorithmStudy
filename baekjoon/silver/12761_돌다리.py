from sys import stdin
from collections import deque

input = stdin.readline


def bfs(start, end):
    queue = deque([start])
    visited = [False] * 100001
    visited[start] = True
    count = 0

    while queue:
        size = len(queue)
        count += 1

        for _ in range(size):
            current = queue.popleft()

            for next_pos in (current - 1, current + 1, current - A, current + A,
                             current - B, current + B, current * A, current * B):
                if next_pos == end:
                    return count

                if 0 <= next_pos <= 100000 and not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append(next_pos)

    return -1


A, B, N, M = map(int, input().split())

start = N
end = M

result = bfs(start, end)

print(result)
