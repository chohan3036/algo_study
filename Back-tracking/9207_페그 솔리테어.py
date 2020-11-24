import sys
read = lambda: sys.stdin.readline().strip()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(pins, depth):
    global min_pin, cnt

    flag = True
    chg_cnt = len(pins)
    while pins:
        x, y = pins.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not 0 <= nx < 5 or not 0 <= ny < 9:
                continue
            if (nx, ny) not in pins:
                continue

            flag = False
            pins.remove((nx, ny))
            pins.add((nx + dx[i], ny + dy[i]))
            dfs(pins, depth + 1)
            pins.add((nx, ny))
            pins.remove((nx + dx[i], ny + dy[i]))

        pins.add((x, y))
        if flag:
            chg_cnt -= 1

        if chg_cnt <= 0:
            break

    if flag:
        if len(pins) < min_pin:
            min_pin = len(pins)
            cnt = depth
        return


for _ in range(int(read())):
    #board = [list(read()) for _ in range(5)]
    board = [['#','#','#','.','.','.','#','#','#'],
            ['.','.','o','o','.','o','.','.','.'],
            ['.','.','.','o','.','o','o','.','.'],
            ['.','.','.','o','o','.','.','.','.'],
            ['#','#','#','.','.','.','#','#','#']]
    pins = set()
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                pins.add((i, j))
    min_pin, cnt = sys.maxsize, sys.maxsize
    dfs(pins, 0)
    print(min_pin, cnt)
