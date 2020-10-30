import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

'''
아기 상어보다 크면 : 못 지나감
아기 상어와 같으면 : 지나감
아기 상어보다 작으면 : 먹을 수 있음
'''


def bfs(x, y, size):
    q = deque([(x, y)])
    sec = [[-1] * n for _ in range(n)]
    sec[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if sec[nx][ny] == -1:
                    if aquarium[nx][ny] <= size:
                        q.append((nx, ny))
                        sec[nx][ny] = sec[cx][cy] + 1
    return sec


def hunt(x, y, size):
    total_time, eaten = 0, 0
    cur_size = size
    cx, cy = x, y
    aquarium[cx][cy] = 0
    while 1:
        fishes = bfs(cx, cy, cur_size)
        dist = 999
        for i in range(n):
            for j in range(n):
                if fishes[i][j] != -1 and fishes[i][j] < dist \
                        and 1 <= aquarium[i][j] < cur_size:
                    dist = fishes[i][j]

        if dist == 999:
            return total_time

        total_time += dist
        eaten += 1

        move = False
        for i in range(n):
            for j in range(n):
                if fishes[i][j] == dist and 1 <= aquarium[i][j] < cur_size:
                    cx, cy = i, j
                    aquarium[i][j] = 0
                    move = True
                    break
            if move:
                break

        if eaten >= cur_size:
            eaten = 0
            cur_size += 1


n = int(read())
aquarium = [list(map(int, read().split())) for _ in range(n)]
bsx, bsy = 0, 0
for i in range(n):
    for j in range(n):
        if aquarium[i][j] == 9:
            bsx, bsy = i, j
            break

print(hunt(bsx, bsy, 2))
