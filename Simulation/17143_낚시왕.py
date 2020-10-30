import sys
read = lambda: sys.stdin.readline().strip()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
change = [1, 0, 3, 2]

r, c, m = map(int, read().split())
water = [[0 for _ in range(c)] for _ in range(r)]
co_sharks = []
for i in range(m):
    x, y, s, d, z = map(int, read().split())
    if d in (1, 2):
        s = s % ((r - 1) * 2)
    else:
        s = s % ((c - 1) * 2)
    co_sharks.append([x - 1, y - 1])
    water[x - 1][y - 1] = [s, d - 1, z]

ans = 0

for col in range(c):
    for i in range(r):
        if water[i][col] != 0:
            ans += water[i][col][2]
            water[i][col] = 0
            co_sharks.pop(co_sharks.index([i, col]))    # 진짜 싫다
            break

    tmp_water = [[0 * c] for _ in range(r)]
    for x, y in co_sharks:
        s, d, z = water[x][y]
        water[x][y] = 0

        # 상어가 도착할 위치 계산
        if d in (0, 1):  # 상 하
            x += dy[d] * s
            for _ in range(2):  # 벽에서 반사 (최대 2번)
                if x < 0:
                    x = -x
                    d = change[d]  # 방향 전환
                elif x >= r:
                    x = (r - 1) * 2 - x
                    d = change[d]
        else:  # 좌 우
            y += dx[d] * s
            for _ in range(2):  # 벽에서 반사 (최대 2번)
                if y < 0:
                    y = -y
                    d = change[d]
                elif y >= c:
                    y = (c - 1) * 2 - y
                    d = change[d]

        if not tmp_water[x][y]:  # 중복 아니면
            tmp_water[x][y] = (s, d, z)
        else:  # 중복이면
            if tmp_water[x][y][2] < z:  # 현재 상어가 더 크면 갱신
                tmp_water[x][y] = (s, d, z)

print(ans)
