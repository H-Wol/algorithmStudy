N, M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums_with_key = []
nums.sort()
for idx, num in enumerate(nums):
    nums_with_key.append([idx, num])

answer = []
answers = []
keys = []


def DFS():
    if len(answer) == M:
        answers.append(" ".join(map(str, answer)))
        return
    for key, num in nums_with_key:
        if key not in keys:
            keys.append(key)
            answer.append(num)
            DFS()
            answer.pop()
            keys.pop()


DFS()


for answer in list(dict.fromkeys(answers)):
    print(answer)
