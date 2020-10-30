N = int(input())
binary = [1, 2]

dp = [0 for i in range(N + 1)]
dp[0] = 1
dp[1] = 2

for i in range(2, N):
     dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N-1])