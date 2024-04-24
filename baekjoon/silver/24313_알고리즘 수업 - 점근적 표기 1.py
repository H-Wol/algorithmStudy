from sys import stdin

input = stdin.readline

a1, a0 = map(int, input().split())
c = int(input().strip())
n0 = int(input().strip())


def check_O_definition(a1, a0, c, n0):
    for n in range(n0, 101):
        f_n = a1 * n + a0
        if f_n > c * n:
            return 0
    return 1


result = check_O_definition(a1, a0, c, n0)
print(result)
