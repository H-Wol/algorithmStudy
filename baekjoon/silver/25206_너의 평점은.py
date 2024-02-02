from sys import stdin
input = stdin.readline

total_credit = 0
credits = 0
score_board = {"A+": 4.5,
               "A0": 4.0,
               "B+": 3.5,
               "B0": 3.0,
               "C+": 2.5,
               "C0": 2.0,
               "D+": 1.5,
               "D0": 1.0,
               "F": 0.0}
for _ in range(20):
    subject, credit, grade = map(str, input().rsplit())
    if grade == "P":
        continue
    credit = float(credit)
    credits += score_board[grade] * credit
    total_credit += credit

print(credits/total_credit)
