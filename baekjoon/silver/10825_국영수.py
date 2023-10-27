from sys import stdin

input = stdin.readline

N = int(input())
students = []

for _ in range(N):
    name, korean, english, math = input().split()
    students.append((name, int(korean), int(english), int(math)))

students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
