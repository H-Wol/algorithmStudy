from sys import stdin

input = stdin.readline


N = int(input())
paper = [[0] * 100 for _ in range(100)]


def count_colored_cells(paper):
    count = 0
    for row in paper:
        count += sum(row)
    return count


for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

result = count_colored_cells(paper)
print(result)
