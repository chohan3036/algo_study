import sys
read = lambda: sys.stdin.readline().strip()

N = int(read())
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]

# pin과 이동의 최소 개수가 매번 변해야..


def pin(i, j, cur_board):
    # 안에서 for문을 돌아야 각 경우의 수 확인 가능

    if cur_board[i][j] == '#' or cur_board[i][j] == '.':
        return

    if i < 0 or j < 0 or i >= 5 or j >= 5:
        return

    for k in range(4):
        next_x = i + x[k]
        next_y = j + y[k]
        next_xx = i + x[k] * 2
        next_yy = j + y[k] * 2

        if 0 < next_xx < 5 and 0 < next_yy < 9:
            if cur_board[next_x][next_y] == 'o' and cur_board[next_xx][next_yy] == '.':
                cur_board[i][j] = '.'
                cur_board[next_x][next_y] = '.'
                cur_board[next_xx][next_yy] = 'o'
                pin(next_xx, next_yy, cur_board)


    pin == min_pin && cnt < min_cnt : min_cnt = cnt


for _ in range(N):
    board = []
    for _ in range(5):
        board.append(list(read()))
