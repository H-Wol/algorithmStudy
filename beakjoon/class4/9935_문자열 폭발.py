from sys import stdin

input = stdin.readline

s = input().rstrip()
bomb = input().rstrip()
bombs = {}
for i, b in enumerate(bomb):
    bombs[b] = i
words = []
answer = []
for i in s:
    if bombs.get(i, None) == None:
        answer.extend(words)
        answer.append(i)
        words = []
        continue
    if bombs.get(i) == 0:
        words.append(i)
        if len(words[-1]) == len(bomb):
            words.pop()
        continue
    if words != [] and bombs.get(i) == len(words[-1]):
        words[-1] += i
        if len(words[-1]) == len(bomb):
            words.pop()
    else:
        answer.extend(words)
        answer.append(i)
        words = []


answer.extend(words)
answer = "".join(answer)
if answer:
    print(answer)
else:
    print("FRULA")
