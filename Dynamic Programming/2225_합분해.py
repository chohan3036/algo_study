n, k = map(int, input().split())
dp = [0] * (n + 1)
dp[0] = 1

for _ in range(1, k + 1):
    for j in range(1, n + 1):
        # 숫자가 하나씩 추가되면서, 그 숫자를 만들 수 있는 경우의 수를 누적시켜 나감
        dp[j] = (dp[j] + dp[j - 1]) % 1000000000

print(dp[n])
