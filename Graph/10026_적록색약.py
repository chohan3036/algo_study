import sys
sys.setrecursionlimit(100000)
reading = lambda: sys.stdin.readline().strip()

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]
rgb = ['R', 'G', 'B']


def dfs_amb(i, j, pre_color):
    global amb
    if i >= N or j >= N or i < 0 or j < 0:
        return
    if chk_amb[i][j]:
        return
    if pre_color != L[i][j]:
        if (pre_color == rgb[2]) | (L[i][j] == rgb[2]):
            return

    chk_amb[i][j] = 1
    for n in range(4):
        dfs_amb(i + x[n], j + y[n], L[i][j])


def dfs_not(i, j, pre_color):
    global not_amb
    if i >= N or j >= N or i < 0 or j < 0:
        return
    if chk_not[i][j]:
        return
    if pre_color != L[i][j]:
        return

    chk_not[i][j] = 1
    for n in range(4):
        dfs_not(i + x[n], j + y[n], L[i][j])


N = int(reading())
L = [list(reading()) for _ in range(N)]
chk_amb = [[0 for _ in range(N)] for _ in range(N)]
chk_not = [[0 for _ in range(N)] for _ in range(N)]
amb, not_amb = 0, 0

for a in range(N):
    for b in range(N):
        if not chk_amb[a][b]:
            amb += 1
            dfs_amb(a, b, L[a][b])
        if not chk_not[a][b]:
            not_amb += 1
            dfs_not(a, b, L[a][b])

print(not_amb, amb)
