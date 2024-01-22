from sys import stdin

input = stdin.readline

N = int(input().strip())
slimes = list(map(int, input().split()))

slimes.sort(reverse=True)

total_damage = 0
current_damage = 0

for i in range(N - 1):
    current_damage += slimes[i]
    total_damage += current_damage * slimes[i + 1]

print(total_damage)
