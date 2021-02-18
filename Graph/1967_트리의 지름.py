import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()


def bfs(start):
    q = deque([start])
    dist = [0 for _ in range(n)]
    visited = set()
    visited.add(start)

    while q:
        cur_node = q.popleft()
        for next_node, w in edges[cur_node]:
            if next_node not in visited:
                dist[next_node] = dist[cur_node] + w
                q.append(next_node)
                visited.add(next_node)
    return dist


n = int(read())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, read().split())
    edges[u - 1].append([v - 1, w])
    edges[v - 1].append([u - 1, w])

# from root -> first farthest
dist_from_root = bfs(0)
left = dist_from_root.index(max(dist_from_root))

# from left -> second farthest
dist_from_left = bfs(left)
print(max(dist_from_left))
