from sys import stdin
input = stdin.readline
tree_dict = {}
total_trees = 0

while True:
    tree = input().rstrip()

    if not tree:
        break

    total_trees += 1
    if tree in tree_dict:
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1

sorted_trees = sorted(tree_dict.items(), key=lambda x: x[0])

for tree, count in sorted_trees:
    percentage = (count / total_trees) * 100
    print(f"{tree} {percentage:.4f}")
