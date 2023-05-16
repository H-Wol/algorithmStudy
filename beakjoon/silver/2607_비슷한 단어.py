from collections import Counter
from sys import stdin

input = stdin.readline


def count_similar_words(words):
    first_word = words[0]
    first_word_freq = Counter(first_word)
    similar_count = 0

    for word in words[1:]:
        word_freq = Counter(word)

        if word_freq == first_word_freq:
            similar_count += 1
        elif len(word) > len(first_word):
            diff_count = sum((word_freq - first_word_freq).values())
            if diff_count <= 1:
                similar_count += 1
        else:
            diff_count = sum((first_word_freq - word_freq).values())
            if diff_count <= 1:
                similar_count += 1

    return similar_count


n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())

result = count_similar_words(words)
print(result)
