x = int(input())
count = 0
while x > 0:
    count += x % 2
    x //= 2

print(count)
