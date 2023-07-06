from sys import stdin

input = stdin.readline


def cal_min_moves(x, y):
    distance = y - x
    count = 0
    move = 1
    total_moves = 0

    while total_moves < distance:
        count += 1
        total_moves += move

        if count % 2 == 0:
            move += 1

    return count


t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    result = cal_min_moves(x, y)
    print(result)
