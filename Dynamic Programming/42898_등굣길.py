def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    # 인덱스가 (1, 1) 시작하니까 1씩 빼주어 dp 배열에 넣음
    # 웅덩이는 -1로 초기화
    for y, x in puddles:
        dp[x - 1][y - 1] = -1

    for i in range(n):
        for j in range(m):
            # 시작점을 1로
            if (i, j) == (0, 0):
                dp[i][j] = 1

            # 웅덩이면 0으로 값 바꾸고 넘어감
            elif dp[i][j] == -1:
                dp[i][j] = 0

            # 웅덩이가 아니면
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1]

                elif j == 0:
                    dp[i][j] = dp[i - 1][j]

                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1] % 1000000007


print(solution(4, 3, [[1, 3], [3, 1]]))
