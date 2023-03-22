import sys
sys.setrecursionlimit(10 ** 9)


# dfs 탐색
def DFS(x, y):
    for a, b in graph[x]:
        if visited[a] == False:
            visited[a] = y + b
            DFS(a, y + b)


V = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]

for _ in range(V):
    line = list(map(int, sys.stdin.readline().split()))
    
    for i in range((len(line)//2)-1):
        graph[line[0]].append([line[i*2+1],line[i*2+2]])
    

visited = [False] * (V + 1)
visited[1] = True
DFS(1, 0)

start = visited.index(max(visited))

visited = [False] * (V + 1)
visited[start] = True
DFS(start, 0)

print(max(visited))
