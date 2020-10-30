# BFS는 그래프다.. 100번 복창
# 최단 거리를 찾는 방법, 즉 문을 연다면 가중치 1을 더해서 뒤로
# 가중치 - 1: 문을 열 때 0: 문을 열지 않을 때
# 가중치 두 개니까 DEQUE 사용
# BFS 중첩해서 하면 시간 복잡도가 너무 큼
# 죄수 하나 이동할 때마다 BFS 도는 거니까 HW*HW 즉 N의 네제곱
# 죄수 1과 죄수 2가 어느 지점에서 만나 밖으로 나간다고 생각하기
# 즉, 밖으로부터, 죄수 1로부터, 죄수 2로부터 '어느 지점'까지 가는 것
# 출발점을 세 개로 나누어 각 배열에 거리 구해놓기
# 이 세 배열을 더하면 됨!! 단, 문 일 때는 가중치 중첩되니까 2 빼줌

import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    dist = [[-1] * w for _ in range(h)]
    q = deque([(x, y)])
    dist[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and prison[nx][ny] != '*':
                if prison[nx][ny] == '#':
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))
                else:
                    dist[nx][ny] = dist[cx][cy]
                    q.appendleft((nx, ny))
    return dist


t = int(read())
for _ in range(t):
    h, w = map(int, read().split())
    prison = ['.' + read() + '.' for _ in range(h)]
    h += 2
    w += 2
    prison = ['.' * w] + prison + ['.' * w]

    prisoner = []
    for i in range(h):
        for j in range(w):
            if prison[i][j] == '$':
                prisoner.append((i, j))

    dist1 = bfs(0, 0)
    dist2 = bfs(prisoner[0][0], prisoner[0][1])
    dist3 = bfs(prisoner[1][0], prisoner[1][1])

    min_dist = h * w    # 999로 했다가 틀렸음 당연하지..
    for i in range(h):
        for j in range(w):
            if prison[i][j] != '*':
                cur = dist1[i][j] + dist2[i][j] + dist3[i][j]
                if prison[i][j] == '#':
                    cur -= 2
                min_dist = min(cur, min_dist)

    print(min_dist)
