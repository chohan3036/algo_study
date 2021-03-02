import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

SIZE = 8

dirs = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
        'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

k, s, n = map(str, read().split())
board = [[0] * SIZE for _ in range(SIZE)]
kx, ky = SIZE - int(k[1]), ord(k[0]) - 65
sx, sy = SIZE - int(s[1]), ord(s[0]) - 65
n = int(n)

moves = deque([read() for _ in range(n)])

while moves:
    cx, cy = dirs[moves.popleft()]
    nx, ny = kx + cx, ky + cy
    if not 0 <= nx < SIZE or not 0 <= ny < SIZE:
        continue
    if nx == sx and ny == sy:
        if not 0 <= sx + cx < SIZE or not 0 <= sy + cy < SIZE:
            continue
        sx += cx
        sy += cy
    kx, ky = nx, ny

print(''.join([chr(ky + 65), str(SIZE - kx)]))
print(''.join([chr(sy + 65), str(SIZE - sx)]))
