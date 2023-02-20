import sys
import re
input = sys.stdin.readline

N, M = map(int, input().split(" "))


pokes = {}
pokesList = []

for i in range(1, N+1):
    name = input().rstrip()
    pokes[name] = i
    pokesList.append(name)


for _ in range(M):
    q = input().rstrip()
    if re.match('[0-9]', q):
        print(pokesList[int(q)-1])
    else:
        print(pokes.get(q))
