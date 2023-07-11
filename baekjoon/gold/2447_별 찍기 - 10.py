n = int(input())


def draw(l):
    if l == 3:
        return ["***", "* *", "***"]

    arr = draw(l // 3)
    stars = []

    for i in arr:
        stars.append(i * 3)

    for i in arr:
        stars.append(i + " " * (l // 3) + i)

    for i in arr:
        stars.append(i * 3)

    return stars


print("\n".join(draw(n)))
