from sys import stdin

input = stdin.readline

n = int(input())
log = set()

for _ in range(n):
    name, status = map(str, input().split())

    if status == 'enter':
        log.add(name)
    else:
        log.remove(name)

result = sorted(log, reverse=True)

for name in result:
    print(name)
