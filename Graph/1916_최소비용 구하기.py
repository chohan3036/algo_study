import sys
from math import inf
from heapq import heappush, heappop
read = lambda: sys.stdin.readline().strip()


def dijkstra(graph, start):
    dist = [inf for _ in range(n)]
    dist[start] = 0
    q = []
    heappush(q, [0, start])
    while q:
        cur_dist, cur_node = heappop(q)
        if dist[cur_node] >= cur_dist:
            for i in range(n):
                new_dist = cur_dist + graph[cur_node][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    heappush(q, [new_dist, i])
    return dist


n = int(read())
m = int(read())
costs = [[inf] * n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, read().split())
    if costs[u - 1][v - 1] != inf and costs[u - 1][v - 1] <= c:
        continue
    costs[u - 1][v - 1] = c
dep, arr = map(int, read().split())
dep, arr = dep - 1, arr - 1

result = dijkstra(costs, dep)
print(result[arr])
