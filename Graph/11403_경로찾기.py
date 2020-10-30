import sys
from collections import deque

reading = lambda: sys.stdin.readline().strip()

N = int(reading())
mat = [list(map(int, reading().split())) for _ in range(N)]
way = [[0 for _ in range(N)] for _ in range(N)]


def bfs(_from, _to):
    queue = deque()
    queue.append(_from)
    visited = set()
    while queue:
        x = queue.popleft()
        visited.add(x)
        _next = mat[x]
        for v in range(len(_next)):
            if _next[v] == 1:
                if v == _to:
                    return 1
            elif v not in visited:
                queue.append(v)
                visited.add(v)
    return 0


for i in range(N):
    for j in range(N):
        way[i][j] = bfs(i, j)
    print(*way[i])
