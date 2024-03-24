from sys import stdin

input = stdin.readline


s = input().strip()

count = [0, 0]

current = s[0]
count[int(current)] += 1


for i in range(1, len(s)):
    if s[i] != current:
        current = s[i]
        count[int(current)] += 1


result = min(count)
print(result)
