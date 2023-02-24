import sys
input = sys.stdin.readline

M = int(input())

answer = 0


def add(ans, x):
    ans = ans | (1 << x)
    return ans


def remove(ans, x):
    ans = ans & ~(1 << x)
    return ans


def toggle(ans, x):
    ans = ans ^ (1 << x)
    return ans


def check(ans, x):
    if ans & (1 << x):
        print(1)
    else:
        print(0)
    return ans


orders = {
    "add": add,
    "remove": remove,
    "toggle": toggle,
    "check": check,

}

for _ in range(M):
    order = input().rstrip()

    if order == "all":
        answer = (1 << 21) - 1
    elif order == "empty":
        answer = 0
    else:
        order, x = order.split(" ")
        func = orders[order]
        answer = func(answer, int(x)-1)
