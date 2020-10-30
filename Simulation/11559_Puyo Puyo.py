import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

PUYO = ['R', 'G', 'B', 'P', 'Y']
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def pop(x, y):
    q = deque([(x, y)])
    visited = set()
    visited.add((x, y))
    color = field[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not 0 <= nx < 12 or not 0 <= ny < 6:
                continue
            if (nx, ny) in visited:
                continue
            if field[nx][ny] == color:
                q.append((nx, ny))
                visited.add((nx, ny))

    if len(visited) >= 4:
        for px, py in visited:
            field[px][py] = '.'
        return True
    else:
        return False


def fall():
    for i in range(10, -1, -1):
        for j in range(6):
            if field[i][j] in PUYO and field[i + 1][j] == '.':
                down = 1
                for k in range(i + 2, 12):
                    if field[k][j] == '.':
                        down += 1
                field[i][j], field[i + down][j] = field[i + down][j], field[i][j]


field = [list(read()) for _ in range(12)]
cnt = 0
while True:
    flag = 0
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] in PUYO:
                if pop(i, j):
                    flag += 1
    if flag > 0:
        cnt += 1
        fall()
    else:
        break

print(cnt)
