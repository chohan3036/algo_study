import sys
reading = lambda :sys.stdin.readline().strip()
x = [0, 0, 1, -1]
y = [-1, 1, 0, 0]

def dfs(i, j, height):
    if i >= N or j >= N or i < 0 or j < 0:
        return
    if A[i][j] <= height:
        return

    A[i][j] = 0
    for k in range(4):
        dfs(i + x[k], j + y[k])

N = int(reading())
A = [list(map(int, reading().split())) for _ in range(N)]
area = []
rain = 1

for i in range(N):
    for j in range(N):
        if A[i][j] != 0:
            dfs(i, j, rain)