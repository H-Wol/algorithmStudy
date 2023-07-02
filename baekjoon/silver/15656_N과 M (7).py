N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()
answer = []


def DFS():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in nums:
        answer.append(i)
        DFS()
        answer.pop()


DFS()
