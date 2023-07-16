from sys import stdin


input = stdin.readline
n = int(input())
buildings = list(map(int, input().split()))


def get_tower(buildings):
    stack = []
    result = []

    for idx, height in enumerate(buildings):
        while stack and stack[-1][1] < height:
            stack.pop()

        if stack:
            result.append(stack[-1][0] + 1)
        else:
            result.append(0)

        stack.append((idx, height))

    return result


answer = get_tower(buildings)

print(" ".join(map(str, answer)))
