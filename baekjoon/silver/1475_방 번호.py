from collections import Counter


room_number = int(input())
digits_count = Counter(str(room_number))
digits_count['6'] = digits_count['9'] = (
    digits_count['6'] + digits_count['9'] + 1) // 2

max_count = max(digits_count.values())
print(max_count)
