from sys import stdin

input = stdin.readline

N = int(input())
students = []

for _ in range(N):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    students.append((name, day, month, year))

students.sort(key=lambda x: (x[3], x[2], x[1]))

print(students[-1][0])
print(students[0][0])
