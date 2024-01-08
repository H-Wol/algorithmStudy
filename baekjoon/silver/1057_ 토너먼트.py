n, kim, lim = map(int, input().split())
rounds = 0

while kim != lim:
    kim = (kim + 1) // 2
    lim = (lim + 1) // 2
    rounds += 1

print(rounds)
