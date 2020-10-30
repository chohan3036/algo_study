import sys
import queue
INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split(' '))
K = int(input())

edge = [] * V
dist = [INF for _ in range(V)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    # 점마다 이어진 간선을 추가해줌
    edge[u - 1].append((v - 1, w))


def dijkstra():
    q = queue.PriorityQueue()
    # 시작 노드 거리 0으로 설정해 삽입
    q.put((0, K - 1))
    dist[K - 1] = 0

    while q:
        pp = q.get()
        cur_v = pp[1]
        cur_d = pp[0]

        # 최소 거리가 저장된 배열에 저장돼 있는 cur_v 까지의 거리와
        # 지금 보고있는 cur_d 를 비교해서
        # 저장돼 있는 거리가 더 짧으면 갱신할 필요 없으므로 continue
        if dist[cur_v] < cur_d:
            continue

        # 이어진 간선들의 거리(지금보고 있는 cur_v를 경유했을 때)를 갱신함
        for next_v, next_d in edge[cur_v]:
            comp_d = cur_d + next_d
            if dist[next_v] > comp_d:
                dist[next_v] = comp_d
                q.put((comp_d, next_v))


dijkstra()
for i in range(V):
    print(dist[i] if dist[i] != INF else "INF")
