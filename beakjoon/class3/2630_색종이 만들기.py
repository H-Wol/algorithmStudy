import sys
input = sys.stdin.readline

N = int(input())

paper = list()

color = {
    0: 0,
    1: 0
}


def is_all_same(paper):
    first_element = paper[0][0]
    for row in paper:
        for element in row:
            if element != first_element:
                return False
    return True


def Quad_tree(paper, size):
    global color
    if size == 1:
        color[part[0][0]] += 1
        return
    size //= 2
    parts = list()
    parts.append([row[:size] for row in paper[:size]])
    parts.append([row[size:] for row in paper[:size]])
    parts.append([row[:size] for row in paper[size:]])
    parts.append([row[size:] for row in paper[size:]])

    for part in parts:
        if is_all_same(part):
            color[part[0][0]] += 1
        else:
            Quad_tree(part, size)
    return


for _ in range(N):

    paper.append(list(map(int, input().split(" "))))

if is_all_same(paper):
    color[paper[0][0]] += 1
else:
    Quad_tree(paper, N)

print(color.get(0))
print(color.get(1))
