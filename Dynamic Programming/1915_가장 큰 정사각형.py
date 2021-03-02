import sys
read = lambda: sys.stdin.readline().strip()

n, m = map(int, read().split())
board = [list(map(int, read())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
            continue

        if board[i][j]:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

ans = 0
for i in range(n):
    ans = max(ans, max(dp[i]))

print(ans * ans)
