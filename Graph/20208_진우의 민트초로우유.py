import sys
read = lambda: sys.stdin.readline().strip()


def dfs(jwx, jwy, hp, milk):
    global ans

    for x, y in milks:
        # 현재까지 마시지 않은 우유인가
        if village[x][y] == 2:
            dist = abs(jwx - x) + abs(jwy - y)
            # 현재 체력으로 도달할 수 있는 위치인가
            if dist <= hp:
                # 보드 위에 이번 우유를 마셨다고 표시
                village[x][y] = 0
                dfs(x, y, hp + h - dist, milk + 1)
                # 복구
                village[x][y] = 2

    if abs(jwx - hx) + abs(jwy - hy) <= hp:
        ans = max(ans, milk)


n, m, h = map(int, read().split())
village = [list(map(int, read().split())) for _ in range(n)]

milks = []      # 우유의 위치를 저장할 리스트
hx, hy = 0, 0   # 집의 위치
for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            hx, hy = i, j
        if village[i][j] == 2:
            milks.append((i, j))

ans = 0
dfs(hx, hy, m, 0)
print(ans)
