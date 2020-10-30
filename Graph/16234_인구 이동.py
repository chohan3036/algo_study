import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    global is_move

    visited = {(i, j)}
    q = deque([(i, j)])

    sum_pop, num = 0, 0

    while q:
        x, y = q.popleft()
        sum_pop += a[x][y]
        num += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    is_move = True

    return int(sum_pop / num), visited


n, l, r = map(int, read().split())
a = [list(map(int, read().split())) for _ in range(n)]
ans = 0


while 1:
    check = set()
    is_move = False
    unions = []

    for i in range(n):
        for j in range(n):
            if (i, j) not in check:
                next_pop, union = bfs(i, j)
                unions.append((union, next_pop))
                check |= union

    if not is_move:
        break

    ans += 1
    for u, pop in unions:
        for i, j in u:
            a[i][j] = pop

print(ans)
