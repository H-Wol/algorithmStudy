from sys import stdin
from collections import deque

input = stdin.readline

N = int(input().rstrip())


def bfs(pos, end, bridge, visited):
    if pos == end:
        return 0
    queue = deque([pos])
    visited[pos] = True
    jump_cnt = 0
    while queue:
        loop_cnt = len(queue)
        jump_cnt += 1
        for _ in range(loop_cnt):
            cur = queue.popleft()
            for next_cur in range(cur, -1, -bridge[cur]):
                if visited[next_cur]:
                    continue
                if next_cur == end:
                    return jump_cnt

                visited[next_cur] = True
                queue.append(next_cur)
            for next_cur in range(cur, N, bridge[cur]):
                if visited[next_cur]:
                    continue
                if next_cur == end:
                    return jump_cnt

                visited[next_cur] = True
                queue.append(next_cur)

    return -1


bridge = list(map(int, input().rsplit()))

a, b = map(int, input().rsplit())
visited = [False for _ in range(N)]
print(bfs(a-1, b-1, bridge, visited))
