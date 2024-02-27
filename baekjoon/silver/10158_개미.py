from sys import stdin

input = stdin.readline

W, H = map(int, input().split())
P, Q = map(int, input().split())
T = int(input())

x = (P + T) % (2 * W)
y = (Q + T) % (2 * H)

x_direction = 1 if (P + T) // W % 2 == 0 else -1
y_direction = 1 if (Q + T) // H % 2 == 0 else -1

final_x = x if 0 <= x < W else W - abs(W - x)
final_y = y if 0 <= y < H else H - abs(H - y)

print(final_x, final_y)
