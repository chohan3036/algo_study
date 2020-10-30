import sys
read = lambda: sys.stdin.readline().strip()


def move(_x, _y, n):
    while board[_x + x[n]][_y + y[n]] != '#' and board[_x + x[n]][_y + y[n]] != 'O':
        _x += x[n]
        _y += y[n]
    return _x, _y


def dfs(r, b, cnt):
    # 두 구슬의 좌표 가지고 dfs 시작
    rx, ry = r
    bx, by = b

    cnt += 1
    if cnt >= 10:
        return -1

    for n in range(4):
        nrx, nry = move(rx, ry, n)
        nbx, nby = move(bx, by, n)

        if board[nrx][nry] == 'O' and board[nbx][nby] == 'O':
            continue
        elif board[nbx][nby] == 'O':
            continue
        elif board[nrx][nry] == 'O':
            return cnt

        if nrx <= 0 or nrx >= N - 1 or nry <= 0 or nry >= M - 1:
            continue
        if nbx <= 0 or nbx >= N - 1 or nby <= 0 or nby >= M - 1:
            continue

        if board[nrx][nry] == '#' and board[nbx][nby] == '#':
            continue
        elif board[nrx][nry] == '#':
            nrx, nry = rx, ry
            if nrx == nbx and nry == nby:
                nbx, nby = bx, by
        elif board[nbx][nby] == '#':
            nbx, nby = bx, by
            if nrx == nbx and nry == nby:
                nrx, nry = rx, ry

        dfs((nrx, nry), (nbx, nby), cnt)
    return


N, M = map(int, read().split())
board = [list(read()) for _ in range(M)]

x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]

R, B = (0, 0), (0, 0)
for i in range(1, N - 1):
    for j in range(1, M - 1):
        # 빨간 구슬 좌표 찾기
        if board[i][j] == 'R':
            R = (i, j)
        # 파란 구슬 좌표 찾기
        elif board[i][j] == 'B':
            B = (i, j)

        if R != (0, 0) and B != (0, 0):
            break

print(dfs(R, B, 0))
