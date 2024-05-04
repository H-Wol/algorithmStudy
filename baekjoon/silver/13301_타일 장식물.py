from sys import stdin

input = stdin.readline

N = int(input())


fibonacci = [1, 1]
perimeter = [4, 6]


for i in range(2, N + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    perimeter.append(perimeter[i - 1] + 2 * fibonacci[i])


print(perimeter[N - 1])
