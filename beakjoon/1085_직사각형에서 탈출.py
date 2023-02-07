x, y, w, h = map(int, input().split())

print((sorted([abs(0-x), abs(x-w), abs(0-y), abs(y-h)]))[0])
print(min(x, y, h-y, w-x)) #개선사항
