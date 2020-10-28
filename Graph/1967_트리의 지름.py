# 트리의 지름 : 어떤 정점으로부터 가장 먼 노드와
# 그 노드로부터 가장 먼 거리에 있는 노드 사이의 거리

import sys
read = lambda: sys.stdin.readline().strip()
from collections import defaultdict, deque


def bfs(_from):
    q = deque([_from])
    visit = set()
    visit.add(_from)

    cur_dist = [0 for _ in range(n + 1)]
    while q:
        cur_node = q.popleft()
        for next_node in tree[cur_node]:
            cur_dist[next_node] += cur_dist[cur_node] + weights[cur_node][next_node]
            q.append(next_node)
            visit.add(next_node)
    return cur_dist


n = int(read())
tree = defaultdict(set)
weights = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, read().split())
    tree[parent].add(child)
    weights[parent][child] = weight

# 루트로부터 가장 먼 노드 찾기
from_root = bfs(1)
print(from_root)
