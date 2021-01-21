import sys
read = lambda: sys.stdin.readline().strip()
move = [(-1, 1), (0, 1), (1, 1)]


def dfs(x, y):
    global ans, board

    if y == c - 1:
        ans += 1
        return True

    for m in move:
        nx, ny = x + m[0], y + m[1]
        if not 0 <= nx < r or not 0 <= ny < c:
            continue
        if board[nx][ny] == 'x':
            continue

        board[nx][ny] = 'x'
        if dfs(nx, ny):
            return True


r, c = map(int, read().split())
board = [list(read()) for _ in range(r)]

ans = 0
for i in range(r):
    board[i][0] = 'x'
    dfs(i, 0)
print(ans)
