from sys import stdin

input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = float("-inf")
min_result = float("inf")


def dfs(index, result, add, subtract, multiply, divide):
    global max_result, min_result

    if index == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add:
        dfs(index + 1, result + numbers[index], add - 1, subtract, multiply, divide)
    if subtract:
        dfs(index + 1, result - numbers[index], add, subtract - 1, multiply, divide)
    if multiply:
        dfs(index + 1, result * numbers[index], add, subtract, multiply - 1, divide)
    if divide:
        dfs(index + 1, int(result / numbers[index]), add, subtract, multiply, divide - 1)


dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_result)
print(min_result)
