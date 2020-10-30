import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def roll(dir, x, y):
    cnt = 0
    # '#' 아닌 경로 끝까지 해당 방향으로 굴림 / 구멍이 아니면
    while board[x + dx[dir]][y + dy[dir]] != '#' and board[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        cnt += 1
    return x, y, cnt


def bfs(x1, y1, x2, y2, depth):
    q = deque([(x1, y1, x2, y2, depth)])
    visited = set()
    visited.add((x1, y1, x2, y2))

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10:
            break

        for i in range(4):
            nrx, nry, r_cnt = roll(i, rx, ry)
            nbx, nby, b_cnt = roll(i, bx, by)

            # 파란 구슬이 탈출했을 경우
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 탈출했을 경우
            if board[nrx][nry] == 'O':
                # 파란 구슬도 탈출하면 안 됨
                if board[nbx][nby] == 'O':
                    continue
                return depth

            # 위치가 겹쳤을 때
            if (nrx, nry) == (nbx, nby):
                if r_cnt > b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1


n, m = map(int, read().split())
#board = [list(read()) for _ in range(n)]
board = [['#','#','#','#','#','#','#'],
         ['#','.','.','.','R','B','#'],
         ['#','.','#','#','#','#','#'],
         ['#','.','.','.','.','.','#'],
         ['#','#','#','#','#','.','#'],
         ['#','O','.','.','.','.','#'],
         ['#','#','#','#','#','#','#']]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j

        elif board[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by, 1))
