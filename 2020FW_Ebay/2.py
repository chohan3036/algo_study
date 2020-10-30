def solution(num, cards):
    dp = [10001 for _ in range(num + 1)]
    dp[0] = 0

    for c in cards:
        for j in range(1, num + 1):
            if j - c >= 0:
                dp[j] = min(dp[j], dp[j - c] + 1)

    return dp[num]


print(solution(8, [1, 4, 6]))
