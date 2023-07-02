from sys import stdin

input = stdin.readline


class Node:
    def __init__(self, val: str):
        self.val = val
        self.left = self.right = None

    def set(self, left, right):
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root: Node):
        self.root = root

    def pre_order(self):
        def _pre_order(node: Node, answer: list):
            if node.val == None:
                return answer
            answer.append(node.val)
            answer = _pre_order(node.left, answer)
            answer = _pre_order(node.right, answer)
            return answer

        print("".join(_pre_order(self.root, [])))

    def in_order(self):
        def _in_order(node: Node, answer: list):
            if node.val == None:
                return answer
            answer = _in_order(node.left, answer)
            answer.append(node.val)
            answer = _in_order(node.right, answer)
            return answer

        print("".join(_in_order(self.root, [])))

    def post_order(self):
        def _post_order(node: Node, answer: list):
            if node.val == None:
                return answer
            answer = _post_order(node.left, answer)
            answer = _post_order(node.right, answer)
            answer.append(node.val)
            return answer

        print("".join(_post_order(self.root, [])))


N = int(input())
nodes = {".": Node(None)}
start = 65
for _ in range(N):
    nodes[chr(start)] = Node(chr(start))
    start += 1
for _ in range(N):
    parent, left, right = map(str, input().rstrip().split())
    nodes[parent].set(nodes[left], nodes[right])


BT = BinaryTree(nodes["A"])
BT.pre_order()
BT.in_order()
BT.post_order()
