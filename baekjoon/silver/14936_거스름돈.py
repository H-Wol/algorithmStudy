from sys import stdin

input = stdin.readline

n = int(input())


if n % 2:
    five_count = n // 5 if (n // 5) % 2 else (n // 5) - 1
else:
    five_count = n // 5 if not (n // 5) % 2 else (n // 5) - 1
if five_count == -1:
    print(-1)
    exit()
lists = [five_count*5 + count*2 for count in range(5)]
if not n in lists:
    print(-1)
else:
    print(lists.index(n)+five_count)
