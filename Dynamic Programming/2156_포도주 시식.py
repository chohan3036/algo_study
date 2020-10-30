# 포도주 시식
# 서로 다른 포도주
# 1. 한 포도주를 선택하면 그 잔에 든 건 다 마심, 마시고 제자리에 다시
# 2. 연속으로 놓인 3잔 마실 수 없음
# 최대한 많이 마시고 싶음

import sys
read = lambda: sys.stdin.readline().strip()

N = int(read())

wines = [0]
for _ in range(N):
    wines.append(int(read()))

dp = [0 for _ in range(N + 1)]
dp[1] = wines[1]
if N >= 2:
    dp[2] = wines[1] + wines[2]
if N >= 3:
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

print(dp[N])
