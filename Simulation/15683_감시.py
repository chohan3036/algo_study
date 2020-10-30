import sys
read = lambda: sys.stdin.readline().strip()
from copy import deepcopy


# 카메라의 작동 함수 만들기
# 방향별로 0 : 위 1 : 오른쪽 2 : 아래 3 : 왼쪽
# map에 감시 가능한 지역을 -1로 만듦
def camera(i, j, dir, mat):
    maps = deepcopy(mat)
    for d in dir:
        # 위
        if d == 0:
            for k in range(i - 1, -1, -1):
                if maps[k][j] == 6:
                    break
                elif maps[k][j] != 0:
                    continue
                maps[k][j] = "#"
        # 오른쪽
        elif d == 1:
            for k in range(j + 1, M):
                if maps[i][k] == 6:
                    break
                elif maps[i][k] != 0:
                    continue
                maps[i][k] = "#"
        # 아래
        elif d == 2:
            for k in range(i + 1, N):
                if maps[k][j] == 6:
                    break
                elif maps[k][j] != 0:
                    continue
                maps[k][j] = "#"
        # 왼쪽
        elif d == 3:
            for k in range(j - 1, -1, -1):
                if maps[i][k] == 6:
                    break
                elif maps[i][k] != 0:
                    continue
                maps[i][k] = "#"
    return maps


def check(mat, cctvs, idx):
    global min_safe

    if idx == len(cctvs):
        value = 0
        for i in range(N):
            value += mat[i].count(0)
        min_safe = min(min_safe, value)
        return

    remain_cctv = cctvs[idx:]
    for i, j in remain_cctv:
        if mat[i][j] == 1:
            for x in range(4):
                next_map = camera(i, j, [x], mat)
                check(next_map, cctvs, idx + 1)

        elif mat[i][j] == 2:
            for x in range(2):
                next_map = camera(i, j, [x, x + 2], mat)
                check(next_map, cctvs, idx + 1)

        elif mat[i][j] == 3:
            for x in range(4):
                next_map = camera(i, j, [x, (x + 1) % 4], mat)
                check(next_map, cctvs, idx + 1)

        elif mat[i][j] == 4:
            for x in range(4):
                next_map = camera(i, j, [x, (x + 1) % 4, (x + 2) % 4], mat)
                check(next_map, cctvs, idx + 1)

        elif mat[i][j] == 5:
            next_map = camera(i, j, [0, 1, 2, 3], mat)
            check(next_map, cctvs, idx + 1)


N, M = map(int, read().split())
office = [list(map(int, read().split())) for _ in range(N)]
cctv = []

# 카메라와 벽의 위치 찾기
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j))

min_safe = N * M
check(office, cctv, 0)
print(min_safe)
