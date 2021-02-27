from math import inf
from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    # 0부터 시작하는 인덱스
    s, a, b = s - 1, a - 1, b - 1

    # inf 로 초기화된 거리행렬
    # 자기 자신으로 가는 간선 가중치는 0
    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    # 거리행렬에 주어진 비용 넣기
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    # 플로이드-와샬
    for k in range(n):          # 1. 모든 노드를 중간점(경로)으로 가정하면서
        for i in range(n):      # 2. 거리행렬을 순회
            for j in range(n):  # 3. 현재 거리행렬에 저장된 거리가 k를 거쳐가는 거리보다 멀면 갱신
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 시간 거의 두 배 걸림..

    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])

    return ans


'''
# 다익스트라
from math import inf
from heapq import heappush, heappop


def dijkstra(n, graph, start):
    dist = [inf for _ in range(n)]  # start 기준의 거리행렬
    dist[start] = 0                 # 자기 자신으로 가는 간선은 0

    q = []
    heappush(q, [dist[start], start])           # 거리와 노드를 함께 큐에 삽입
    while q:                                    # (비용이 작은 노드를 먼저 선택)
        cur_dist, cur_dest = heappop(q)
        if dist[cur_dest] >= cur_dist:          # start에서 cur_dest로 가는 거리가
            for i in range(n):                  # 이미 저장된 거리보다 작을 때만 진행
                new_dist = cur_dist + graph[cur_dest][i]
                if new_dist < dist[i]:          # cur_dest를 거쳐 i로 가는 거리가
                    dist[i] = new_dist          # 이미 저장된 거리보다 작으면 갱신
                    heappush(q, [new_dist, i])  # 다음 인접한 노드를 고려하기 위해 큐에 삽입
    return dist


def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1   # 0부터 시작하는 인덱스
    graph = [[inf] * n for _ in range(n)]
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    # 다익스트라
    # 모든 노드에 대해 다익스트라를 수행하고,
    # 반환된 1차원 거리행렬을 append 해줌
    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))

    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, min_graph[s][k] + min_graph[k][a] + min_graph[k][b])

    return ans
'''


print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7],
                            [6, 5, 11], [2, 5, 12], [5, 3, 20],
                            [2, 4, 8], [4, 3, 9]]))
