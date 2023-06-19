import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = Node(value)
                break
            else:
                current = current.right

    return root


def post_order(root):
    if root is None:
        return

    stack = []
    result = []
    current = root

    while True:
        while current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left

        current = stack.pop()

        if current.right and stack and stack[-1] == current.right:
            stack.pop()
            stack.append(current)
            current = current.right
        else:
            result.append(current.value)
            current = None

        if not stack:
            break

    for value in result:
        print(value)


def solve(inputs):
    root = None
    for value in inputs:
        root = insert(root, value)

    post_order(root)


if __name__ == "__main__":
    inputs = []
    for line in sys.stdin:
        value = int(line.strip())
        inputs.append(value)

    solve(inputs)
