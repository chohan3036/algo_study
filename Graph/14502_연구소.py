import sys
read = lambda: sys.stdin.readline().strip()
from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, read().split())
maps, empty_wall, virus = [], [], []
dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    tmp = list(map(int, read().split()))
    for j in range(M):
        # 벽 좌표를 저장
        if tmp[j] == 0:
            empty_wall.append((i, j))
        # 바이러스 좌표 저장
        elif tmp[j] == 2:
            virus.append((i, j))
    # 원본 map 구성
    maps.append(tmp)


def count_zero(maps):
    count = 0
    for x in range(N):
        for y in range(M):
            if maps[x][y] == 0:
                count += 1
    return count


def bfs(start, candidate, maps):
    # bfs 돌기 전에 원본 map 보존
    tmp_map = deepcopy(maps)

    # 구해놓은 벽 조합 가지고 시작
    for x, y in candidate:
        tmp_map[x][y] = 1
    queue = deque()
    queue.extend(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dir_x[i], y + dir_y[i]
            # if 조건문에서 꼭 범위 먼저 써주기!! ★★★
            if 0 <= nx < N and 0 <= ny < M and tmp_map[nx][ny] == 0:
                tmp_map[nx][ny] = 2
                queue.append((nx, ny))
    return count_zero(tmp_map)


# 벽 조합 구하기
candidates = list(combinations(empty_wall, 3))

max_value = 0
for i in candidates:
    result = bfs(virus, list(i), maps)
    if max_value < result:
        max_value = result

print(max_value)
