import sys
reading = lambda: sys.stdin.readline().strip()

N, M = map(int, reading().split())
mat = [list(reading()) for _ in range(N)]
board_BW = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
board_WB = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
_min = 64

for i in range(N - 7):
    for j in range(M - 7):
        cnt_bw = 0
        # BW
        for x in range(8):
            for y in range(8):
                if mat[i + x][j + y] != board_BW[x][y]:
                    cnt_bw += 1
        cnt_wb = 0
        # WB
        for x in range(8):
            for y in range(8):
                if mat[i + x][j + y] != board_WB[x][y]:
                    cnt_wb += 1
        _min = min(cnt_bw, cnt_wb, _min)

print(_min)
