import sys
read = lambda: sys.stdin.readline().strip()

N = int(read())
dp = [0, 1]
for i in range(2, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[N])

# 개수 세 보면 그렇더라고요
