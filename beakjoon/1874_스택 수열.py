n = int(input())
stack = [1]
answer = ["+"]
failFlag = False


def stacks():
    global failFlag
    cur = -1
    source = 2
    for num in range(n):
        target = int(input())
        if failFlag:
            continue
        while cur != target:
            if target >= source:
                stack.append(source)
                answer.append("+")
                source += 1
            else:
                if stack != []:
                    answer.append("-")
                    cur = stack.pop()
                else:
                    failFlag = True
                    break
    return failFlag


stacks()
if failFlag:
    print("NO")
else:
    for i in answer:
        print(i)
