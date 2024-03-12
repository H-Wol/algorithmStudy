from sys import stdin

input = stdin.readline

scores = [int(input()) for _ in range(8)]

score_with_index = [(score, index + 1) for index, score in enumerate(scores)]

score_with_index.sort(reverse=True)

selected_scores = score_with_index[:5]
total_score = sum(score for score, _ in selected_scores)
indices = sorted(index for _, index in selected_scores)

print(total_score)
print(*indices)
