import sys

input = sys.stdin.readline

N = int(input())

having = {}

cards = map(int, input().split(" "))

for card in cards:

    having[card] = 1

M = int(input())

finds = map(int, input().split(" "))

answers =[]

for find in finds:

    answers.append(having.get(find, 0))

print(" ".join(map(str,answers)))
