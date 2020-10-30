n, num = map(int, input().split())
cards = [int(input()) for _ in range(n)]

dp = [10001 for _ in range(num + 1)]
dp[0] = 0

for c in cards:
    for j in range(1, num + 1):
        if j - c >= 0:
            dp[j] = min(dp[j], dp[j - c] + 1)

print(dp[num]) if dp[num] != 10001 else print(-1)
