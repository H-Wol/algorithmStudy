from collections import deque

n = int(input())


def dfs(n):
    queue = deque(range(1, 10))
    if n < 10:
        return n
    count = 9
    while count < n:
        num = queue.popleft()
        last_digit = num % 10
        for i in range(last_digit):
            new_num = num * 10 + i
            queue.append(new_num)
            count += 1
            if count == n:
                return new_num
    return -1


if n >= 1023:
    print(-1)
else:
    print(dfs(n))
