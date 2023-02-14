import sys
input = sys.stdin.readline
N = int(input())

sum = 0
nums = []
num_dict = {}


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
        if (left[l] < right[h]):
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[h])
            h += 1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list


for _ in range(N):
    num = int(input())
    nums.append(num)
    sum += num

avg = sum/N
print(round(avg))


sorted_nums = merge_sort(nums)

print(sorted_nums[round(N//2)])

for num in sorted_nums:
    num_dict[num] = num_dict.get(num, 0)+1

if (N == len(num_dict)):
    if N > 1:
        print(sorted_nums[1])
    else:
        print(sorted_nums[0])
else:
    max_cnt = max(num_dict.values())
    max_cnts = []
    for k, v in num_dict.items():
        if v == max_cnt:
            max_cnts.append(k)
    if len(max_cnts) > 1:
        print(max_cnts[1])
    else:
        print(max_cnts[0])


print(sorted_nums[-1] - sorted_nums[0])
