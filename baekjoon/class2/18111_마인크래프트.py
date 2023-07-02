from collections import Counter
N, M, B = map(int, input().split())
maps = list()
for i in range(N):
    maps += list(map(int, input().split()))


time = 100000000
height = 0
maxBlocks = sum(maps) + B
minHeight = min(maps)
maxHeight = max(maps)
maps = dict(Counter(maps))

for currentHeight in range(minHeight, maxHeight+1):
    if maxBlocks < currentHeight * N * M:
        continue
    reqTime = 0
    for i in maps:
        if i >= currentHeight:
            reqTime += 2*(i - currentHeight) * maps[i]
        else:
            reqTime += (currentHeight - i) * maps[i]
    if reqTime <= time:
        time = reqTime
        height = currentHeight
print(time, height)
