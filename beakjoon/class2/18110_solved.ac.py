from sys import stdin


def calc_avg(scores):
    def round(val):
        return int(val) + 1 if val - int(val) >= 0.5 else int(val)

    scores.sort()
    nn = round(n * 0.15)
    print(round(sum(scores[nn:-nn] if nn else scores) / (n - 2 * nn)))


input = stdin.readline
n = int(input())
if n:
    scores = []
    for _ in range(n):
        score = int(input())
        scores.append(score)

    calc_avg(scores)

else:
    print(0)
