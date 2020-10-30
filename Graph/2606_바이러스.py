import sys

def dfs(graph, start):
    visit = []
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return len(visit) - 1

N = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = [list() for _ in range(N + 1)]
for _ in range(E):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
print(dfs(graph, 1))