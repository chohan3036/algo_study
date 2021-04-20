import sys
read = lambda: sys.stdin.readline().strip()
from heapq import heappush, heappop
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(x, y):
    q = deque([(x, y)])
    dp = [[0] * m for _ in range(n)]
    dp[x][y] = 0

    while q:
        cx, cy = q.popleft()

        if cx == n and cy == m:
            return dp[cx][cy]

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not 0 <= nx < n or not 0 <= ny < m:
                continue
            if arr[nx][ny] >= arr[cx][cy]:
                continue

            if dp[nx][ny] == -1:
                dp[nx][ny] = dp[cx][cy]
            else:
                dp[nx][ny] = dp[cx][cy] + 1


n, m = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(n)]

print(bfs(0, 0))
