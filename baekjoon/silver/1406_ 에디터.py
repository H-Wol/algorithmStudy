from sys import stdin

input = stdin.readline


class Node:
    def __init__(self, data, next=None, front=None):
        self.data = data
        self.next = next
        self.front = front


datas = list(input().rstrip())
nodes = [Node(datas[0])]
HEAD = nodes[0]

for i in range(1, len(datas)):
    node = Node(datas[i], None, nodes[-1])
    nodes[-1].next = node
    nodes.append(node)

node = Node(None, None, nodes[-1])
nodes[-1].next = node
nodes.append(node)

cur = nodes[-1]

M = int(input())


def L(cur: Node):
    if cur.front == None:
        return cur
    return cur.front


def D(cur: Node):
    if cur.next == None:
        return cur
    return cur.next


def B(cur: Node):
    global HEAD
    if cur.front == None:
        return cur
    if cur.front.front == None:
        cur.front = None
        HEAD = cur
        return cur
    if cur.front.front == HEAD:
        HEAD = cur
    cur.front.front.next = cur
    cur.front = cur.front.front
    return cur


def P(cur: Node, s: str):
    global HEAD
    node = Node(s, cur, cur.front)
    nodes.append(node)
    if cur.front == None:
        cur.front = node
        HEAD = node
        return cur
    cur.front.next = node
    cur.front = node
    return cur


func = {
    "L": L,
    "D": D,
    "B": B,
    "P": P,
}

for _ in range(M):
    inputs = input().rstrip()
    if inputs.startswith("P"):
        cur = P(cur, inputs.split()[-1])
    else:
        cur = func[inputs](cur)

if HEAD == None or HEAD.data == None:
    print("")
    exit()

answer = []

while True:
    answer.append(HEAD.data)
    HEAD = HEAD.next
    if HEAD == None or HEAD.data == None:
        break
print("".join(answer))
