import sys
read = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)


def dfs(node):
    visited[node] = 1
    if node in graph:
        for next in graph[node]:
            if not visited[next]:
                dfs(next)


n, m = map(int, read().split())
graph = dict()
ans = 0
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, read().split())
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    graph[u].add(v)
    graph[v].add(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)
