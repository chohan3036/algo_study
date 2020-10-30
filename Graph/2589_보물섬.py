import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, depth):
    q = deque([(x, y, depth)])
    visited = set()
    visited.add((x, y))

    cur_dist = -1
    while q:
        cx, cy, cd = q.popleft()
        for i in range(4):
            nx, ny, nd = cx + dx[i], cy + dy[i], cd + 1
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if not board[nx][ny] == 'L':
                continue
            if (nx, ny) in visited:
                continue
            q.append((nx, ny, nd))
            visited.add((nx, ny))
            cur_dist = max(cur_dist, nd)

    return cur_dist


r, c = map(int, read().split())
board = [list(read()) for _ in range(r)]
max_dist = -1

for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            max_dist = max(max_dist, bfs(i, j, 0))

print(max_dist)
