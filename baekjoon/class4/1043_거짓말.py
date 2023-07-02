from sys import stdin

input = stdin.readline


N, M = map(int, input().split())

truth_knowers = set(map(int, input().split()[1:]))

parties = []

for _ in range(M):
    party = set(map(int, input().split()[1:]))
    parties.append(party)

truth_count = 0

while True:
    updated = False
    remove_list = []

    for party in parties:
        if truth_knowers.intersection(party):
            updated = True
            remove_list.append(party)
            truth_knowers.update(party)

    if not updated:
        break

    for party in remove_list:
        parties.remove(party)

for party in parties:
    if not truth_knowers.intersection(party):
        truth_count += 1

print(truth_count)
