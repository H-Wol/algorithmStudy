from collections import deque, defaultdict
from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
origins = nums[:]
nums = deque(nums)
tmp = deque([nums.popleft()])
answers = defaultdict(lambda: deque([]))
while nums:
    flag = False

    target = nums.popleft()
    while tmp:
        if tmp[-1] < target:
            answers[tmp.pop()].append(target)
            continue
        else:
            break
    tmp.append(target)


for num in origins:
    if answers[num]:
        print(answers[num].popleft(), end=" ")
    else:
        print(-1, end=" ")
