import sys
read = lambda: sys.stdin.readline().strip()
n = 10


def back_tracking(x, y, r, c):
    nx, ny = x + r, x + c
    if canvas[nx][ny] == 1:
        for k in range(5, 1, -1):
            canvas[nx][ny] = k
            nr, nc = r, c
            if nx - x == k - 1 and ny - y == k - 1:
                return True
            elif nx - x < k and ny - y == k - 1:
                nr += 1
                nc = 0
            else:
                nc += 1

            if back_tracking(x, y, nr, nc):
                return True
            canvas[x][y] = 1


canvas = [list(map(int, read().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if canvas[i][j]:
            back_tracking(i, j, 0, 0)

print(canvas)
