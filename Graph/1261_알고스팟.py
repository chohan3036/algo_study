import sys
from heapq import heappush, heappop

read = lambda: sys.stdin.readline().strip()
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dijkstra(cnt, x, y):
    crashed = [[-1] * m for _ in range(n)]
    crashed[0][0] = 0

    q = []
    heappush(q, (cnt, x, y))

    while q:
        cur_cnt, cx, cy = heappop(q)
        if cx == n - 1 and cy == m - 1:
            break

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not 0 <= nx < n or not 0 <= ny < m:
                continue
            if crashed[nx][ny] >= 0:
                continue
            crashed[nx][ny] = cur_cnt
            if maze[nx][ny] == '1':
                heappush(q, (cur_cnt + 1, nx, ny))
            else:
                heappush(q, (cur_cnt, nx, ny))

    return crashed


m, n = map(int, read().split())
maze = [list(read()) for _ in range(n)]

ans = dijkstra(0, 0, 0)
print(ans[n - 1][m - 1])
