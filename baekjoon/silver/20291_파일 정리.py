from sys import stdin


input = stdin.readline
N = int(input())
files = [input().rstrip() for _ in range(N)]
file_types = {}

for file in files:
    _, file_extension = file.split(".")
    if file_extension in file_types:
        file_types[file_extension] += 1
    else:
        file_types[file_extension] = 1

sorted_file_types = sorted(file_types.items())

for file_type, count in sorted_file_types:
    print(f"{file_type} {count}")
