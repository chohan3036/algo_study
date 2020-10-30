from collections import deque
import sys
readline = lambda: sys.stdin.readline().strip()

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
L, D = (3, 2, 0, 1), (2, 3, 1, 0)


def snake():
    x, y, z, d, sec = 0, 0, 0, 0, 0
    A[0][0] = 2
    q = deque()
    q.append((0, 0))

    while True:
        x, y = x + dx[d], y + dy[d]
        sec += 1

        if x < 0 or x >= N or y < 0 or y >= N or A[x][y] == 2:
            print(sec)
            return

        if not A[x][y]:
            nx, ny = q.popleft()
            A[nx][ny] = 0
        A[x][y] = 2
        q.append((x, y))
        t, c = B[z]

        if sec == int(t):
            if c == 'L':
                d = L[d]
            else:
                d = D[d]
            z = (z + 1) % M


N = int(readline())
A = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(int(readline())):
    u, v = map(int, readline().split())
    A[u - 1][v - 1] = 1
M = int(readline())
B = [list(readline().split()) for _ in range(M)]
snake()
