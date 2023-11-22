from sys import stdin

input = stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
words.sort()

count = 0
last_word = words[0]

for word in words[1:]:
    if not word.startswith(last_word):
        count += 1
    last_word = word


print(count + 1)
