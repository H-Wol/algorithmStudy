message = input()

MOD = 1000000


n = len(message)
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if message[i - 1] != "0":
        dp[i] += dp[i - 1]

    if i >= 2:
        two_digits = int(message[i - 2 : i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    dp[i] %= MOD

print(dp[n])
