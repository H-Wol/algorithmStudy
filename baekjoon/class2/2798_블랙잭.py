n, _max = map(int, input().split())
data = list(map(int, input().split()))

temp = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            r = data[i]+data[j]+data[k]
            if temp < r <= _max:
                temp = r

print(temp)
