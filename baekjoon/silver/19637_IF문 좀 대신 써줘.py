from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

legendary = []
categories = []

for _ in range(N):
    name, power = input().split()
    power = int(power)
    legendary.append(name)
    categories.append(power)


def find_category(legendary, categories, num):
    low, high = 0, len(categories) - 1

    while low < high:
        mid = (low + high) // 2
        if num > categories[mid]:
            low = mid + 1
        else:
            high = mid

    return legendary[low]


for _ in range(M):
    query = int(input())
    result = find_category(legendary, categories, query)
    print(result)
