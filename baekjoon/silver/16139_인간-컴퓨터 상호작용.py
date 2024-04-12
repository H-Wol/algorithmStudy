from sys import stdin

input = stdin.readline


S = (input().rstrip())

q = int(input().rstrip())

questions = list()
str_length = len(S)
counter = [[] for _ in range(26)]


for i in range(97, 123):
    cnt = 0
    for j in range(str_length):
        if S[j] == chr(i):
            cnt += 1
        counter[i-97].append(cnt)

for _ in range(q):
    a, l, r = map(str, input().rsplit())
    a, l, r = ord(a)-97, int(l), int(r)
    if S[l] == chr(a+97):
        print(counter[a][r] - counter[a][l] + 1)
    else:
        print(counter[a][r] - counter[a][l])
