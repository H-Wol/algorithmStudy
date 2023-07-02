target = int(input())
cur, cnt = 1, 1
while cur < target:
    cur += cnt * 6
    cnt += 1
print(cnt)
