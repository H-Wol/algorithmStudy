from sys import stdin

input = stdin.readline


chosen_numbers = []
max_len_numbers = []


def DFS(v):
    global max_len_numbers
    visited[v] = True

    chosen_numbers.append(v)
    for i in nodes[v]:
        if not visited[i]:
            if not nodes[i] or i == v:
                continue
            DFS(i)
        elif i in chosen_numbers:
            max_len_numbers += chosen_numbers[chosen_numbers.index(i):]
            chosen_numbers.pop()
            return
    chosen_numbers.pop()


N = int(input())
visited = [False for _ in range(101)]

nodes = [[]for _ in range(101)]
self_numbers = []

for i in range(N):
    number = int(input())
    if number == i+1:
        self_numbers.append(number)
        continue
    nodes[number].append(i+1)


for i in range(1, N+1):
    chosen_numbers = []
    DFS(i)
answer = list(set(max_len_numbers + self_numbers))
print(len(answer))
for i in sorted(answer):
    print(i)
