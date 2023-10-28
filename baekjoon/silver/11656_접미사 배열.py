from sys import stdin

input = stdin.readline

word = input().rstrip()
suffixes = [word[i:] for i in range(len(word))]
suffixes.sort()

for suffix in suffixes:
    print(suffix)
