import sys
input = sys.stdin.readline

N = int(input())

map = list()


def is_all_same(map):
    first_element = map[0][0]
    for row in map:
        for element in row:
            if element != first_element:
                return False
    return True


def Quad_tree(map, size):
    size //= 2
    quad = ["("]
    parts = list()
    parts.append([row[:size] for row in map[:size]])
    parts.append([row[size:] for row in map[:size]])
    parts.append([row[:size] for row in map[size:]])
    parts.append([row[size:] for row in map[size:]])

    for part in parts:
        if is_all_same(part):
            quad.append(part[0][0])
        else:
            quad.extend(Quad_tree(part, size))
    quad.append(")")
    return quad


for _ in range(N):
    lst = [int(c) for c in input().rstrip()]
    map.append(lst)

if is_all_same(map):
    print(map[0][0])
else:
    print(''.join(str(item) for item in Quad_tree(map, N)))
