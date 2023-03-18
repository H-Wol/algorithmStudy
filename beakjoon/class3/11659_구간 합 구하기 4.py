import sys
input = sys.stdin.readline  

N, M = map(int, input().split(" ")) 

numbers = list(map(int, input().split(" ")))
prefix_sum = [0]
sum = 0
for i in numbers:
    sum += i
    prefix_sum.append(sum)
for _ in range(M):
    x,y = map(int, input().split(" ")) 
    print(prefix_sum[y] - prefix_sum[x-1])