import sys

input = sys.stdin.readline

N = int(input())

members = []


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
        idx = 0
        if left[l][idx] == right[h][idx]:
            idx = 2
        if (left[l][idx] < right[h][idx]):
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[h])
            h += 1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list


for i in range(N):
    members.append(list(map(str, input().rstrip().split(" "))))
    members[-1].append(i)
    members[-1][0] = int(members[-1][0])
members = merge_sort(members)
for member in members:
    print(member[0], member[1])
