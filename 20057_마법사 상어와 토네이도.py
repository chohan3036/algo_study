import sys
read = lambda: sys.stdin.readline().strip()


def sand(x, y):
    rest_sand = arr[x][y]
    for i in range(10):
        spr_sand = int(rest_sand * ss[i] // 100)
        arr[x + sx][y + sy] += spr_sand
        rest_sand -= spr_sand




n = int(read())
arr = [list(map(int, read().split())) for _ in range(n)]
tx, ty = [0, 1, 0, -1], [-1, 0, 1, 0]
sx, sy = [1, 1, 1, 2], [-1, 0, 1, 0]
ss = [10, 7, 1, 2]

