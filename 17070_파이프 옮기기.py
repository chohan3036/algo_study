import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

move = [[(0, 1), (1, 1)],
        [(1, 0), (1, 1)],
        [(0, 1), (1, 0), (1, 1)]]


def bfs(x, y):
    q = deque([(x, y, 0)])
    cnt = 0

    while q:
        cx, cy, cd = q.popleft()
        for i in range(len(move[cd])):
            dx, dy = move[cd][i]
            nx, ny = cx + dx, cy + dy
            if not 0 <= nx < n or not 0 <= ny < n:
                continue

            flag = False
            if (dx, dy) == (1, 1):
                for x, y in [(0, 1), (1, 0)]:
                    gx, gy = cx + x, cx + y
                    if house[gx][gy]:
                        flag = True
                        break

            if nx == n - 1 and ny == n - 1:
                cnt += 1
                continue

            if flag:
                continue
            q.append((nx, ny, i))

    return cnt


n = int(read())
house = [list(map(int, read().split())) for _ in range(n)]
print(bfs(0, 1))

