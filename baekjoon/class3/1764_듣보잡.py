import sys
input = sys.stdin.readline


N,M = map(int,input().split(" "))

n = list()
m = list()

for _ in range(N):
    n.append(input().rstrip())
    
for _ in range(M):
    m.append(input().rstrip())
    
    
dup = list(set(n) & set(m))
dup.sort()
print(len(dup))
for i in dup:
    print(i)

