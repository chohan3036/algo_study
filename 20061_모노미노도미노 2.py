import sys
read = lambda: sys.stdin.readline().strip()

shapes = {1: [(0, 0)],
          2: [(0, 0), (0, 1)],
          3: [(0, 0), (1, 0)]}

board_blue = [[0] * 10 for _ in range(4)]
board_green = [[0] * 4 for _ in range(10)]

n = int(read())
dominoes = [tuple(map(int, read().split())) for _ in range(n)]

score = 0


def move(x, y):
    # 각 블록을 한 칸씩 이동해서 가능한 위치를 찾음
    moved_col, moved_row = 9, 9
    for dx, dy in shapes[t]:
        nx, ny = x + dx, y + dy

        # 파란색 보드로 이동
        col = ny
        while col < 9 and board_blue[nx][col + 1] != 1:
            col += 1
        if col < moved_col:
            moved_col = col

        # 초록색 보드로 이동
        row = nx
        while row < 9 and board_green[row + 1][ny] != 1:
            row += 1
        if row < moved_row:
            moved_row = row

    board_blue[x][moved_col] = 1
    board_green[moved_row][y] = 1
    if t == 2:
        board_blue[x][moved_col - 1] = 1
        board_green[moved_row][y + 1] = 1
    elif t == 3:
        board_blue[x + 1][moved_col] = 1
        board_green[moved_row - 1][y] = 1


def full():
    global score

    # 한 줄이 다 찼는지 검사
    for i in range(6, 10):
        if all(board_blue_t[i]):
            score += 1
            board_blue_t[i] = [0, 0, 0, 0]
            board_blue_t[5: i + 1] = board_blue_t[4: i]

    for i in range(6, 10):
        if all(board_green[i]):
            score += 1
            board_green[i] = [0, 0, 0, 0]
            board_green[5: i + 1] = board_green[4: i]


def soft():
    # 연한 칸에 있는지
    soft_blue = 2 - (any(board_blue_t[4]) + any(board_blue_t[5]))
    if soft_blue < 2:
        board_blue_t[6:] = board_blue_t[4 + soft_blue: 8 + soft_blue]
        board_blue_t[4 + soft_blue: 6] = [[0, 0, 0, 0]] * (2 - soft_blue)

    soft_green = 2 - (any(board_green[4]) + any(board_green[5]))
    if soft_green < 2:
        board_green[6:] = board_green[4 + soft_green: 8 + soft_green]
        board_green[4 + soft_green: 6] = [[0, 0, 0, 0]] * (2 - soft_green)


for t, x, y in dominoes:
    move(x, y)
    board_blue_t = list(map(list, zip(*board_blue)))
    full()
    soft()
    board_blue = list(map(list, zip(*board_blue_t)))

blocks = 0
for i in range(4):
    blocks += sum(board_blue[i])
for i in range(10):
    blocks += sum(board_green[i])

print(score)
print(blocks)
