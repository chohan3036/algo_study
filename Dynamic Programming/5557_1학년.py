import sys
read = lambda: sys.stdin.readline().strip()

N = int(read())
num = list(map(int, read().split()))

dp = [[0 for _ in range(21)] for _ in range(N - 1)] # 0부터 20까지만 안다고 했으니까

for i in range(N - 1):
    if i == 0:
        dp[i][num[i]] = 1
        continue

    for j in range(21):
        pre = dp[i - 1][j]
        if pre != 0:
            if j - num[i] >= 0:
                dp[i][j - num[i]] += pre
            if j + num[i] <= 20:
                dp[i][j + num[i]] += pre

print(dp[N - 2][num[N - 1]])

# https://dev-wd.github.io/algorithm/backjoon5557/