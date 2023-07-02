from sys import stdin

input = stdin.readline

s1, s2 = [0], [0]

s1.extend(list(input().rstrip()))
s2.extend(list(input().rstrip()))


arr = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            arr[i][j] = 0
        elif s1[i] == s2[j]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[-1][-1])
