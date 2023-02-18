import sys
input = sys.stdin.readline

oddLine = ["W", "B"] * 4
evenLine = ["B", "W"] * 4

standard = [oddLine, evenLine] * 4
reversedStandard = [evenLine, oddLine] * 4
N, M = map(int, input().split(" "))

target = []
for _ in range(N):
    target.append(list(map(str, input().rstrip())))


def compare(row: list, rowNum: int):
    global standard, reversedStandard
    drawCnt = 0
    reversedDrawCnt = 0
    for i in range(8):
        if standard[rowNum][i] != row[i]:
            drawCnt += 1
        if reversedStandard[rowNum][i] != row[i]:
            reversedDrawCnt += 1
    return drawCnt, reversedDrawCnt


count = sys.maxsize
for row in range(8, N+1, 1):
    for col in range(8, M+1, 1):
        drawCnt = 0
        reversedDrawCnt = 0
        for i in range(row-8, row):
            x, y = compare(target[i][col-8:col], i-(row-8))
            drawCnt += x
            reversedDrawCnt += y
        count = min([count, drawCnt, reversedDrawCnt])
print(count)
