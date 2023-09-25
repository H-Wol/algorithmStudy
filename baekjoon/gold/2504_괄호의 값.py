from sys import stdin

input = stdin.readline


def evaluate_brackets(s):
    stack = []

    for char in s:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            temp = 0
            flag = True
            while stack:
                top = stack.pop()
                if top == "(":
                    flag = False
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(temp * 2)
                    break
                elif top == "[":
                    print(0)
                    return
                else:
                    temp += top
            if flag:
                print(0)
                return
        elif char == "]":
            temp = 0
            flag = True
            while stack:
                top = stack.pop()
                if top == "[":
                    flag = False
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(temp * 3)
                    break
                elif top == "(":
                    print(0)
                    return
                else:
                    temp += top
            if flag:
                print(0)
                return
        else:
            print(0)
            return

    result = 0
    for item in stack:
        if item == "(" or item == "[":
            print(0)
            return
        result += item

    print(result)


brackets = input().strip()
evaluate_brackets(brackets)
