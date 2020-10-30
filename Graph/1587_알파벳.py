# 각 경로를 그냥 추가하면 되네..
import sys
read = lambda: sys.stdin.readline().strip()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global ans
    q = {(x, y, board[x][y])}

    while q:
        cx, cy, string = q.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] not in string:
                    q.add((nx, ny, string + board[nx][ny]))
                    ans = max(ans, len(string) + 1)


#r, c = 2, 4
#board = [['C','A','A','B'], ['A','D','C','B']]
r, c = map(int, read().split())
board = [list(read()) for _ in range(r)]
ans = 1
bfs(0, 0)
print(ans)
