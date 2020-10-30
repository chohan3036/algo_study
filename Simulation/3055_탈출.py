import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(mat, stt):
    queue = deque(stt)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 'X':
                continue
            if board[nx][ny] == '*':
                continue

            # 경로에 도달하는 시간 계산
            if mat[x][y] != -1 and mat[nx][ny] == -1:
                queue.append((nx, ny))
                mat[nx][ny] = mat[x][y] + 1

    return mat


#r, c = map(int, read().split())
#board = [list(read()) for _ in range(r)]
r, c = 3, 3
board = [['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']]

wtr_board = [[-1] * c for _ in range(r)]
water = []

dist = [[-1] * c for _ in range(r)]
start = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            end = (i, j)
        elif board[i][j] == 'S':
            dist[i][j] = 0
            start.append((i, j))
        elif board[i][j] == '*':
            wtr_board[i][j] = 0
            water.append((i, j))


print(bfs(wtr_board, water))

print(bfs(dist, start))
