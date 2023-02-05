people = int(input())
start, end = map(int, input().split())
loops = int(input())


def BFS(start, end):
    distance = [0] * (people+1)
    visited[start] = 1
    bfs.append(start)
    queue = [start]

    while (queue):
        start = queue.pop(0)
        for i in node[start]:
            if end in node[start]:
                i = end
            if (visited[i] == 0):
                visited[i] = 1
                bfs.append(i)
                queue.append(i)
                distance[i] = distance[start] + 1
                if i == end:
                    queue.clear()
                    return distance[i]
    return -1


bfs = []


node = [[]for _ in range(people+1)]
visited = [0]*(people+1)

for i in range(loops):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

print(BFS(start, end))
