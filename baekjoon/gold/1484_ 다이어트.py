G = int(input())
answers = []
divisors = []
divisors2 = []
for i in range(1, int(G ** (1 / 2) + 1)):
    if G % i == 0:
        divisors.append(i)
        divisors2.append(int(G / i))
for d1, d2 in zip(divisors, divisors2):
    for start in range(1, G):
        end = start - d1
        if end <= 0:
            continue
        if start + end == d2:
            answers.append(start)
            break
if answers == []:
    print(-1)
    exit()
answers.sort()
for answer in answers:
    print(answer)
