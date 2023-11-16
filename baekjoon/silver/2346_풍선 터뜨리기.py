

N = int(input())
balloons_info = list(map(int, input().split()))

balloons = list(enumerate(balloons_info, start=1))
result = []

current_index = 0
while balloons:
    move = balloons[current_index][1]
    result.append(balloons.pop(current_index)[0])

    if not balloons:
        break

    if move > 0:
        current_index = (current_index + move - 1) % len(balloons)
    else:
        current_index = (current_index + move) % len(balloons)

print(*result)
