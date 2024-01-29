from sys import stdin

input = stdin.readline

_, _ = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def merge_arrays(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


result = merge_arrays(arr1, arr2)
print(" ".join(map(str, result)))
