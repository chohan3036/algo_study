import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
rotate = {'L': [3, 0, 1, 2], 'D': [1, 2, 3, 0]}


def snake():
    global time

    body = deque([(0, 0)])
    dir = 1

    while True:
        time += 1
        cx, cy = body[0]
        nx, ny = cx + dx[dir], cy + dy[dir]

        if not 0 <= nx < n or not 0 <= ny < n:
            return time

        for x, y in body:
            x += dx[dir]
            y += dy[dir]

        if (nx, ny) in body:
            return time

        body.appendleft((nx, ny))

        if (nx, ny) in apples:
            apples.remove((nx, ny))
        else:
            body.pop()

        if paths and time == int(paths[0][0]):
            l_r = paths[0][1]
            dir = rotate[l_r][dir]
            paths.pop(0)


n = int(read())
k = int(read())
apples = []
for _ in range(k):
    x, y = map(int, read().split())
    apples.append((x - 1, y - 1))
l = int(read())
paths = [tuple(map(str, read().split())) for _ in range(l)]
time = 0
print(snake())
