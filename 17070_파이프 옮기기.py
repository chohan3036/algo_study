import sys
read = lambda: sys.stdin.readline().strip()

n = int(read())
house = [list(map(int, read().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][2] = 1

for i in range(n):
    for j in range(2, n):
        if house[i][j] != 1:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if house[i - 1][j] != 1 and house[i][j - 1] != 1:
                dp[i][j][2] = sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))
