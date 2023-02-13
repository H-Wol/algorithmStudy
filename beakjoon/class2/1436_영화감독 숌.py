import sys
N = int(sys.stdin.readline())
num = 665

while N:
    num += 1
    if '666' in str(num):
        N -= 1
print(num)
