from sys import stdin

input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0

for i in range(N):
    left, right = 0, N - 1
    target = numbers[i]

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            if left != i and right != i:
                count += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1

print(count)
