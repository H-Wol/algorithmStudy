s = input().strip()

substrings = set()
n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        substr = s[i:j]
        substrings.add(substr)

print(len(substrings))
