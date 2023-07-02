import sys
import re
input = sys.stdin.readline
isNotBracket = re.compile('[A-Za-z.\s]')

while True:
    sen = input().rstrip()
    if sen == ".":
        break
    brackets = []
    yesFlag = True
    for s in sen:
        if isNotBracket.match(s):
            continue
        elif s == '[':
            brackets.append(1)
        elif s == '(':
            brackets.append(2)
        elif s == ']' and len(brackets) != 0:
            if brackets.pop() != 1:
                yesFlag = False
                break
        elif s == ')' and len(brackets) != 0:
            if brackets.pop() != 2:
                yesFlag = False
                break
        else:
            yesFlag = False
            break
    if yesFlag and len(brackets) == 0:
        print('yes')
    else:
        print('no')
