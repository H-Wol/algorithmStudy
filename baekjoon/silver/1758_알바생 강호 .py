from sys import stdin

input = stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]


tips.sort(reverse=True)
total_tip = sum(max(tip - idx, 0) for idx, tip in enumerate(tips))


print(total_tip)
