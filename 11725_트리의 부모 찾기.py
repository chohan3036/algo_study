import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs(num):
    q = deque([num])
    visit = set()

    while q:
        cur_parent = q.popleft()
        for n1, n2 in nodes:
            if (n1, n2) in visit:
                continue

            if n1 == cur_parent:
                parents[n2] = n1
                q.append(n2)
                visit.add((n1, n2))

            elif n2 == cur_parent:
                parents[n1] = n2
                q.append(n1)
                visit.add((n1, n2))


n = int(read())
nodes = [tuple(map(int, read().split())) for _ in range(n - 1)]

parents = [0 for _ in range(n + 1)]
bfs(1)
for i in range(2, n + 1):
    print(parents[i])
