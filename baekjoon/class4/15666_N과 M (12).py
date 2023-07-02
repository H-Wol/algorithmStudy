N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums_with_key = []
nums.sort()

answer = []
answers = {}
keys = []


def DFS():
    if len(answer) == M:
        answers[" ".join(map(str, (answer)))] = 1
        return
    for num in nums:
        if len(answer) == 0 or answer[-1] <= num:
            answer.append(num)
            DFS()
            answer.pop()


DFS()


for answer in answers:
    print(answer)
