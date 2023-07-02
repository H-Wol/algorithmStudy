N, M = map(int, input().split(" "))
nums = sorted(list(map(int, input().split(" "))))
answer = []


def DFS():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(N):
        if nums[i] not in answer:
            answer.append(nums[i])
            DFS()
            answer.pop()
DFS()
