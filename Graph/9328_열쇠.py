# 처음 생각
# 문서 최대 개수, 즉 최단 거리 X, 가능한 것 다 찾기
# 그럼 출발점은?
# 가장 자리가 '.'이거나 문일 경우(열쇠가 있다면)
# 그럼 BFS를 최대 2 * H * W - 4 번 돌겠지? 정수번

import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global keys

    q = deque([(x, y)])
    visit = set()
    doc = 0
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*':
                # 빈 공간이면 경로에 추가
                if arr[nx][ny] == '.':
                    q.append((nx, ny))

                # 문이면 열쇠 유무 검사
                elif arr[nx][ny].isupper() and arr[nx][ny].lower() in keys:
                    q.append((nx, ny))

                # 열쇠면 줍줍 (중복 방지)
                elif arr[nx][ny].islower() and arr[nx][ny] not in keys:
                    keys += arr[nx][ny]

                elif arr[nx][ny] == '$' and (nx, ny) not in visit:
                    doc += 1
                    visit.add((nx, ny))

    return doc


t = int(read())
for _ in range(t):
    h, w = map(int, read().split())
    #arr = [read() for _ in range(h)]
    #keys = read()
    arr = ['*****************',
           '.............**$*',
           '*B*A*P*C**X*Y*.X.',
           '*y*x*a*p**$*$**$*',
           '*****************']
    keys = 'cz'

    start = set()

    for i in range(h):
        if i == 0 or i == h - 1:
            for j in range(w):
                if arr[i][j] == '.':
                    start.add((i, j))
                elif arr[i][j].isupper() and arr[i][j].lower() in keys:
                    start.add((i, j))
        else:
            for j in (0, w - 1):
                if arr[i][j] == '.':
                    start.add((i, j))
                elif arr[i][j].isupper() and arr[i][j].lower() in keys:
                    start.add((i, j))

    max_doc = 0
    for x, y in start:
        cur_doc = bfs(x, y)
        max_doc = max(max_doc, cur_doc)

    print(max_doc)
