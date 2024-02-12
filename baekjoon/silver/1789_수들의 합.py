S = int(input())
current_sum = 0
count = 1

while current_sum + count <= S:
    current_sum += count
    count += 1

print(count - 1)
