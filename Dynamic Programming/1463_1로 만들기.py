import sys
readline = lambda: sys.stdin.readline().strip()

X = int(readline())
dp = [0 for _ in range(X + 1)]

for i in range(2, X + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[X])
