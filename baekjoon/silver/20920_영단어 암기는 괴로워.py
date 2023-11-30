from sys import stdin
from collections import Counter

input = stdin.readline
n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]


def memorize_words(words, m):
    word_count = Counter(words)
    sorted_words = sorted(
        word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

    result = []
    for word in sorted_words:
        if len(word) >= m:
            result.append(word)

    return result


result = memorize_words(words, m)

for word in result:
    print(word)
