'''
from math import factorial

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // factorial(m - n) // factorial(n))
'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * m for _ in range(n)]
    dp[0] = [i + 1 for i in range(m)]

    for i in range(1, n):
        for j in range(i, m):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    print(dp[n - 1][m - 1])
