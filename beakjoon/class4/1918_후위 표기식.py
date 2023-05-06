from sys import stdin

sen = stdin.readline().rstrip()

answers = []
exps = []


exp_score = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 2, ")": 2}

for s in sen:
    if s not in exp_score:
        answers.append(s)
        continue
    if len(exps) == 0 or s == "(":
        exps.append(s)
        continue
    if s == ")":
        while exps:
            if exps[-1] == "(":
                exps.pop()
                break
            else:
                answers.append(exps.pop())
        continue
    if s == "+" or s == "-":
        while exps and exps[-1] != "(":
            answers.append(exps.pop())
        exps.append(s)
        continue
    if s == "*" or s == "/":
        while exps and exp_score[exps[-1]] == 1:
            answers.append(exps.pop())
        exps.append(s)
        continue

while exps:
    answers.append(exps.pop())
print("".join(answers))
