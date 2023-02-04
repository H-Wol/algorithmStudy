target = list(map(int, input().split()))

asc = sorted(target)
desc = sorted(target, reverse=True)

if target == asc:
    print("ascending")
elif target == desc:
    print("descending")
else:
    print("mixed")