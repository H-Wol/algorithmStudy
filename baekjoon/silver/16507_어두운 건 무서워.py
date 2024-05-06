from sys import stdin

input = stdin.readline

R, C, Q = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(R)]


prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        prefix_sum[i][j] = (
            image[i - 1][j - 1]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]
        )


for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    sum_rect = (
        prefix_sum[r2][c2]
        - prefix_sum[r1 - 1][c2]
        - prefix_sum[r2][c1 - 1]
        + prefix_sum[r1 - 1][c1 - 1]
    )
    num_pixels = (r2 - r1 + 1) * (c2 - c1 + 1)
    avg_value = sum_rect // num_pixels
    print(avg_value)
