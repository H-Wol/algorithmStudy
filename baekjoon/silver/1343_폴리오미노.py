from sys import stdin

input = stdin.readline

board = input().strip()

board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
