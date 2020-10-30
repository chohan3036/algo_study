import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def spread():
    # 확산되는 곳에 이미 먼지가 있을 수도 있기 때문에
    # 더해질 먼지들을 다 누적시킨 후에 나중에 더해줌
    # 동시에 일어나는 일이니까!
    temp_map = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if area[i][j] >= 5:
                dirt = area[i][j] // 5
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and area[nx][ny] != -1:
                        temp_map[nx][ny] += dirt
                        area[i][j] -= dirt

    for i in range(r):
        for j in range(c):
            area[i][j] += temp_map[i][j]


def clean(x):
    for i in range(x - 2, -1, -1):  # 위, 아래
        area[i + 1][0] = area[i][0]

    for j in range(1, c):   # 위, 왼
        area[0][j - 1] = area[0][j]

    for i in range(1, x + 1):   # 위, 위
        area[i - 1][c - 1] = area[i][c - 1]

    for j in range(c - 2, 0, -1):   # 위, 오른
        area[x][j + 1] = area[x][j]
    area[x][1] = 0

    for i in range(x + 3, r):   # 아래, 위
        area[i - 1][0] = area[i][0]

    for j in range(1, c):   # 아래, 왼
        area[r - 1][j - 1] = area[r - 1][j]

    for i in range(r - 2, x, -1):   # 아래, 아래
        area[i + 1][c - 1] = area[i][c - 1]

    for j in range(c - 2, 0, -1):   # 아래, 오른
        area[x + 1][j + 1] = area[x + 1][j]
    area[x + 1][1] = 0


r, c, t = map(int, read().split())
area = [list(map(int, read().split())) for _ in range(r)]
vacuum = 0
for i in range(r):
    for j in range(1):
        if area[i][j] == -1:
            vacuum = i
            break
    if vacuum != 0:
        break

for x in range(t):
    spread()
    clean(vacuum)

print(sum(map(sum, area)) + 2)
