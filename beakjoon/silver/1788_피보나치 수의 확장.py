fib_memo = [0, 1]

N = int(input())

for _ in range(2, abs(N) + 1):
    fib_memo.append((fib_memo[-1] + fib_memo[-2]) % 1000000000)

if fib_memo[abs(N)] == 0:
    print(0)
else:
    if N > 0 or (N < 0 and N % 2):
        print(1)
    else:
        print(-1)
print(fib_memo[abs(N)] % 1000000000)
