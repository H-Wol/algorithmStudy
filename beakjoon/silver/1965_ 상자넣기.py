from sys import stdin

input = stdin.readline


n = int(input())


boxes = list(map(int, input().split()))

answers = {boxes[0]: 1}


for i in range(1, n):
    cur = boxes[i]
    cnts = [x for i, x in answers.items() if i < cur]
    if cnts == []:
        answers[cur] = 1
        continue
    cnt = max(cnts) + 1
    if answers.get(cur, 0) < cnt:
        answers[cur] = cnt

print(max([x for x in answers.values()]))
