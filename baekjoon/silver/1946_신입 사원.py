from sys import stdin

input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    applicants.sort()
    interviews_passed = 1
    min_interview_rank = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < min_interview_rank:
            interviews_passed += 1
            min_interview_rank = applicants[i][1]

    print(interviews_passed)
