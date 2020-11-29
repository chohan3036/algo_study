import sys
sys.setrecursionlimit(10**9)
read = lambda: sys.stdin.readline().strip()
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(pins):
    global min_pin, visit

    print(pins)

    if pins in visit:
        return

    if len(pins) < min_pin:
        min_pin = len(pins)

    for pin in pins[::-1]:
        x, y = pin
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            nnx, nny = nx + dx[i], ny + dy[i]
            if (nx, ny) not in pins:
                continue
            if not 0 <= nnx < 5 or not 0 <= nny < 9:
                continue
            if board[nnx][nny] == '#':
                continue
            if (nnx, nny) in pins:
                continue

            pins.remove((x, y))
            pins.remove((nx, ny))
            pins.append((nx + dx[i], ny + dy[i]))
            dfs(pins)
            pins.append((x, y))
            pins.append((nx, ny))
            pins.remove((nx + dx[i], ny + dy[i]))


for _ in range(int(read())):
    #board = [list(read()) for _ in range(5)]
    board = [['#','#','#','.','o','.','#','#','#'],
             ['.','.','.','o','.','o','.','.','.'],
             ['.','o','o','.','o','.','o','.','.'],
             ['.','o','.','.','.','.','.','.','.'],
             ['#','#','#','.','.','.','#','#','#']]
    pins = []
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                pins.append((i, j))
    org_pin, min_pin = len(pins), len(pins)
    visit = []
    dfs(pins)
    print(min_pin, org_pin - min_pin)
