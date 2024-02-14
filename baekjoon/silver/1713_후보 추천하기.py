from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())

recommended = []


class Student:
    def __init__(self, id, recommend_count, time_added):
        self.id = id
        self.recommend_count = recommend_count
        self.time_added = time_added


students = [Student(int(student_id), 0, i)
            for i, student_id in enumerate(input().split())]


for student in students:
    found = False
    for i in range(len(recommended)):
        if recommended[i].id == student.id:
            recommended[i].recommend_count += 1
            found = True
            break

    if not found:
        if len(recommended) < N:
            recommended.append(Student(student.id, 1, student.time_added))
        else:
            recommended.sort(key=lambda x: (
                x.recommend_count, x.time_added))
            recommended.pop(0)
            recommended.append(Student(student.id, 1, student.time_added))

recommended.sort(key=lambda x: x.id)
result = [student.id for student in recommended]
print(*result)
