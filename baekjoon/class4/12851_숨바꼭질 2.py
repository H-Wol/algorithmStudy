from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())


def moveable(x):
    return x - 1, x + 1, 2 * x


visited = [False for _ in range(100002)]

counts = {}


def BFS(start, end, visited):
    queue = deque([start])
    visited[N] = True
    cnt = 0
    flag = False
    answers = []
    available = {}
    answer = 0
    if start == end:
        return 0, 1
    while not flag:
        size = len(queue)
        cnt += 1
        for _ in range(size):
            forward = queue.popleft()

            for cur in moveable(forward):
                if cur < 0 or cur > 100001:
                    continue
                if cur == end:
                    # answers.append(forward)
                    answer += counts.get(forward, 1)
                    flag = True
                    continue

                if visited[cur] != True:
                    visited[cur] = True
                    available[cur] = True
                    counts[cur] = counts.get(forward, 1)
                    queue.append(cur)
                    continue
                if available.get(cur, None):
                    counts[cur] = counts.get(forward, 1) + counts.get(cur, 0)
        available = {}
    # for a in list(set(answers)):
    #     answer += counts.get(a, 1)
    return cnt, answer


answer = BFS(N, K, visited)
for i in answer:
    print(i)
