import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs(num):
    q = deque([num])
    visit = {num}

    while q:
        cur_parent = q.popleft()
        for node in nodes[cur_parent]:
            if node not in visit:
                parents[node] = cur_parent
                q.append(node)
                visit.add(node)


n = int(read())
nodes = dict()
for _ in range(n - 1):
    n1, n2 = map(int, read().split())
    if n1 not in nodes:
        nodes[n1] = set()
    if n2 not in nodes:
        nodes[n2] = set()
    nodes[n1].add(n2)
    nodes[n2].add(n1)

parents = [0 for _ in range(n + 1)]
bfs(1)
for i in range(2, n + 1):
    print(parents[i])
