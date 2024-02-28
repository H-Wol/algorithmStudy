from sys import stdin
from collections import deque

input = stdin.readline


def postfix_evaluation(expression, values):
    stack = deque()

    for char in expression:
        if char.isalpha():
            stack.append(values[ord(char) - ord('A')])
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    return stack.pop()


N = int(input())
expression = input().rstrip()
values = [int(input()) for _ in range(N)]

result = postfix_evaluation(expression, values)
print("{:.2f}".format(result))
