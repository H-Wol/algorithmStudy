from sys import stdin

input = stdin.readline


N = int(input().strip())
line = list(map(int, input().split()))


def is_possible(arrangement):
    stack = []
    current_order = 1

    for student in arrangement:
        if student == current_order:
            current_order += 1
        else:
            while stack and stack[-1] == current_order:
                stack.pop()
                current_order += 1
            stack.append(student)

    while stack and stack[-1] == current_order:
        stack.pop()
        current_order += 1

    return current_order == len(arrangement) + 1


if is_possible(line):
    print("Nice")
else:
    print("Sad")
