N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()
answer = []


def DFS():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in nums:
        if len(answer) == 0 or answer[-1] <= i:
            answer.append(i)
            DFS()
            answer.pop()


DFS()
