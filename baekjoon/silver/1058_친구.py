from sys import stdin

input = stdin.readline


n = int(input())
graph = [input().strip() for _ in range(n)]
max_friends = 0


def count_direct_friends(graph, person):
    count = 0
    for friend in graph[person]:
        if friend == 'Y':
            count += 1
    return count


for i in range(n):
    friends = set()
    for j in range(n):
        if i != j and graph[i][j] == 'Y':
            friends.add(j)

            for k in range(n):
                if i != k and j != k and graph[j][k] == 'Y':
                    friends.add(k)

    max_friends = max(max_friends, len(friends))

print(max_friends)
