def solution(n):
    dp = [0] * (n + 2)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 2):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567


print(solution(1))
