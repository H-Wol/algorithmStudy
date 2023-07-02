from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input().strip())

    found = False
    for i in range(n):
        for j in range(n):
            if i == j:
                continue 

            candidate = strings[i] + strings[j]
            if candidate == candidate[::-1]:
                print(candidate)
                found = True
                break
        if found:
            break

    if not found:
        print("0")
