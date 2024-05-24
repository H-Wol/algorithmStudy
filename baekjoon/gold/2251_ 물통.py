from sys import stdin
from collections import deque

input = stdin.readline

A, B, C = map(int, input().split())


queue = deque([(0, 0, C)])
check = [[False] * 201 for _ in range(201)]
answers = [False for _ in range(201)]


def BFS(queue, answers):
    while queue:
        a, b, c = queue.popleft()

        if check[a][b] == True:
            continue

        check[a][b] = True

        if a == 0:
            answers[c] = True

        # A->B
        if a + b > B:
            queue.append([a + b - B, B, c])
        else:
            queue.append([0, a + b, c])

        # A->C
        if a + c > C:
            queue.append([a + c - C, b, C])
        else:
            queue.append([0, b, a + c])

        # B->C
        if b + c > C:
            queue.append([a, b + c - C, C])
        else:
            queue.append([a, 0, b + c])

        # B->A
        if b + a > A:
            queue.append([A, b + a - A, c])
        else:
            queue.append([b + a, 0, c])

        # C->A
        if c + a > A:
            queue.append([A, b, c + a - A])
        else:
            queue.append([a + c, b, 0])

        # C->B
        if c + b > B:
            queue.append([a, B, c + b - B])
        else:
            queue.append([a, c + b, 0])
    return answers


answers = BFS(queue, answers)

for idx, val in enumerate(answers):
    if val:
        print(idx, end=" ")
