from sys import stdin


input = stdin.readline

T = int(input())


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


def find_existence(note1, note2):
    note1.sort()

    for num in note2:
        result = binary_search(note1, num)
        print(result)


for _ in range(T):
    _ = int(input())
    note1 = list(map(int, input().split()))
    _ = int(input())
    note2 = list(map(int, input().split()))

    find_existence(note1, note2)
