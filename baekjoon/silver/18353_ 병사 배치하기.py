from sys import stdin

input = stdin.readline

N = int(input())
soldiers = list(map(int, input().split()))


def find_lis(arr):
    lis = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)


lis = find_lis(soldiers)
result = N - lis

print(result)
