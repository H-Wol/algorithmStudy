def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


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
