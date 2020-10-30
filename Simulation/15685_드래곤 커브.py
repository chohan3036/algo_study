import sys
read = lambda: sys.stdin.readline().strip()

n = int(read())
curves = [[0] * 101 for _ in range(101)]

dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

for _ in range(n):
    # 행렬로 바꾸면 거꾸로 y, x
    y, x, d, g = map(int, read().split())

    # 지금 좌표, 방향에 따른 다음 좌표 리스트에 넣고 1로 표시
    total_array = [(x, y), (x + dx[d], y + dy[d])]
    curves[x][y] = 1
    curves[x + dx[d]][y + dy[d]] = 1

    # g세대 동안
    for generation in range(g):
        add_array = []  # 새로 추가될 좌표
        lx, ly = total_array[-1][0], total_array[-1][1] # 가장 마지막 좌표
        for px, py in total_array[len(total_array) - 2::-1]:
            nx = lx - (ly - py)
            ny = ly + (lx - px)
            # 맵을 벗어나는가?
            if not (0 <= nx <= 100 and 0 <= ny <= 100): break
            curves[nx][ny] = 1  # curves 업데이트 (드래곤 커브가 지나가는 곳)
            add_array.append((nx, ny))
        # 원래 드래곤 커브에다가 새로 생긴 드래곤 커브를 더
        total_array.extend(add_array)
        add_array.clear()

cnt = 0
for i in range(100):
    for j in range(100):
        if not curves[i][j] == 1: continue
        if not curves[i][j + 1] == 1: continue
        if not curves[i + 1][j] == 1: continue
        if curves[i + 1][j + 1] == 1: cnt = cnt + 1
print(cnt)
