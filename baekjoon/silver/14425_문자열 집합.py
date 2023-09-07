from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

string_set = set()

for _ in range(n):
    string = input()
    string_set.add(string)

count = 0
for _ in range(m):
    query = input()
    if query in string_set:
        count += 1

print(count)
