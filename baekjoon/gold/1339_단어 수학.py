from collections import defaultdict
from sys import stdin

input = stdin.readline

N = int(input().strip())
words = [input().strip() for _ in range(N)]

letter_weight = defaultdict(int)

for word in words:
    length = len(word)
    for i in range(length):
        letter_weight[word[i]] += 10 ** (length - i - 1)

sorted_weights = sorted(letter_weight.values(), reverse=True)

result, digit = 0, 9
for weight in sorted_weights:
    result += weight * digit
    digit -= 1

print(result)
