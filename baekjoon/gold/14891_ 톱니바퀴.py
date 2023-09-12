from sys import stdin

input = stdin.readline


n, m = map(int, input().split())
lessons = list(map(int, input().split()))


left, right = max(lessons), sum(lessons)


def check(mid, lessons, m):
    cnt = 1
    total = 0

    for lesson in lessons:
        if total + lesson <= mid:
            total += lesson
        else:
            cnt += 1
            total = lesson

    return cnt <= m


while left <= right:
    mid = (left + right) // 2
    if check(mid, lessons, m):
        right = mid - 1
    else:
        left = mid + 1

print(left)
