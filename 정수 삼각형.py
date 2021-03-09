def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        m = len(triangle[i])
        for j in range(m):
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
            elif j == m - 1:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i - 1][j] + triangle[i][j], triangle[i - 1][j - 1] + triangle[i][j])

    return max(triangle[n - 1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
