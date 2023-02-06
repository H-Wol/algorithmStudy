nums = list(map(int, input().split()))
validations = 0
sum = 0
for num in nums:
    sum += num**2
validations = sum % 10
print(validations)
