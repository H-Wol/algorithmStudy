from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arrangement = list(input().rstrip())
count = 0
for i in range(N):
    if arrangement[i] == 'P':
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if arrangement[j] == 'H':
                arrangement[j] = 'X'
                count += 1
                break
print(count)
