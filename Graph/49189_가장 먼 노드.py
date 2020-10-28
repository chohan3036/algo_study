from collections import deque


def solution(n, edge):
    graph = dict()
    for n1, n2 in edge:
        if n1 not in graph:
            graph[n1] = set()
        graph[n1].add(n2)

        if n2 not in graph:
            graph[n2] = set()
        graph[n2].add(n1)

    stt, cnt = 1, 0
    q = deque([[stt, cnt]])
    visit = [-1] * (n + 1)
    while q:
        node, dist = q.popleft()
        visit[node] = dist
        if node in graph:
            for next_node in graph[node]:
                if visit[next_node] == -1:
                    visit[next_node] = 0
                    q.append([next_node, dist + 1])

    return visit.count(max(visit))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
