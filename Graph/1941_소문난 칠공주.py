import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque
from itertools import combinations
from itertools import product


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(team):
    q = deque(team)
    visited = set()

    while q:
        x, y = q.popleft()
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if not 0 <= nx < 5 or not 0 <= ny < 5:
                continue
            if (nx, ny) in team:
                


    return True


seats = [list(read()) for _ in range(5)]
idx = list(product([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]))
comb = combinations(idx, 7)

ans = 0
for c in comb:
    s, y = 0, 0
    flag = True
    for i, j in c:
        if seats[i][j] == 'S':
            s += 1
        else:
            y += 1

        if y > 3:
            flag = False
            break

    if flag and bfs(c):
        ans += 1

print(ans)
