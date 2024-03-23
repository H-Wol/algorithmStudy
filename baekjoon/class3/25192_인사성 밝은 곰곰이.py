from sys import stdin

input = stdin.readline

N = int(input())

cnt = 0
new_chat_list = set()
for _ in range(N):
    record = input().strip()

    if record == "ENTER":
        cnt += len(new_chat_list)
        new_chat_list = set()
    else:
        new_chat_list.add(record)
cnt += len(new_chat_list)
print(cnt)
