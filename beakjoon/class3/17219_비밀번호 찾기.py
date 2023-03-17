import sys
input = sys.stdin.readline

N, M = map(int, input().split(" ")) 

pwd = dict()
for _ in range(N):
    k,v = map(str, input().rstrip().split(" ")) 
    pwd[k] = v

for _ in range(M):
    print(pwd.get(input().rstrip()))