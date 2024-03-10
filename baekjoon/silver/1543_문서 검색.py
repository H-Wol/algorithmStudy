from sys import stdin

input = stdin.readline

document = input().rstrip()
search_word = input().rstrip()

count = 0
index = 0

while index <= len(document) - len(search_word):
    if document[index:index+len(search_word)] == search_word:
        count += 1
        index += len(search_word)
    else:
        index += 1

print(count)
