def isRightTriangle(x, y, z):
    sides = sorted([x, y, z])
    if (sides[0]**2 + sides[1]**2) != sides[2] ** 2:
        print("wrong")
        return 0
    print("right")


while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    isRightTriangle(x, y, z)
