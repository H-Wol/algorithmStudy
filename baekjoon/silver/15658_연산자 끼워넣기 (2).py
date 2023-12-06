from sys import stdin

input = stdin.readline

N = int(input())
numbers = list(map(int, input().rsplit()))
operators = list(map(int, input().rsplit()))

max_result = float('-inf')
min_result = float('inf')


def dfs(index, current, add, subtract, multiply, divide):
    global max_result, min_result

    if index == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    if add > 0:
        dfs(index + 1, current + numbers[index],
            add - 1, subtract, multiply, divide)
    if subtract > 0:
        dfs(index + 1, current - numbers[index],
            add, subtract - 1, multiply, divide)
    if multiply > 0:
        dfs(index + 1, current * numbers[index],
            add, subtract, multiply - 1, divide)
    if divide > 0:
        if current >= 0:
            dfs(index + 1, current //
                numbers[index], add, subtract, multiply, divide - 1)
        else:
            dfs(index + 1, -(-current //
                numbers[index]), add, subtract, multiply, divide - 1)


dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_result)
print(min_result)
