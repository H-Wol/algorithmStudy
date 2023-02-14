import sys

L = int(sys.stdin.readline())
str = sys.stdin.readline().rstrip()


def hashing(a, r, i):
    return a * (r ** i)


answer = 0

for i in range(L):
    answer += hashing(ord(str[i])-96, 31, i)
print(answer % 1234567891)
