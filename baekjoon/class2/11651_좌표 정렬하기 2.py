import sys


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    merged_list = []
    l = h = 0
    while l < len(left) and h < len(right):
        idx = 1
        if left[l][idx] == right[h][idx]:
            idx = 0
        if (left[l][idx] < right[h][idx]):
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[h])
            h += 1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list


input = sys.stdin.readline

N = int(input())

dots = []

for _ in range(N):
    dots.append(list(map(int, input().split(" "))))

dots = merge_sort(dots)
for dot in dots:
    print(dot[0], dot[1])
