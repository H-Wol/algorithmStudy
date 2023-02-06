def reverse(str):
    return int(str[::-1])
x, y = map(reverse, input().split())
print(x if x > y else y)
