import sys
read = lambda: sys.stdin.readline().strip()

ans = []
t = int(read())
for _ in range(t):
    n = int(read())
    dp = [0] * 12
    dp[0] = 1
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    ans.append(dp[n])

for a in ans:
    print(a)
