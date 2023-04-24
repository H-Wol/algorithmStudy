from sys import stdin


formula = stdin.readline().rstrip()

nums = formula.split("-")
total = sum(list(map(int, nums[0].split("+"))))
for idx in range(1, len(nums)):
    total -= sum(list(map(int, nums[idx].split("+"))))
print(total)
