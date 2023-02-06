str = input().upper()

counts = dict()
max = 0
for i in str:
    counts[i] = counts.get(i, 0) + 1
    if counts[i] > max:
        max = counts[i]

keys = [k for k, v in counts.items() if v == max]
if (len(keys) > 1):
    print("?")
else:
    print(keys[0])
