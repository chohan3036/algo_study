import sys
read = lambda: sys.stdin.readline().strip()


def chk(i, j, num):
    # 가로줄
    if num in board[i]:
        return False

    # 세로줄
    if num in tp[j]:
        return False

    # 3*3 네모칸
    x, y = i // 3 * 3, j // 3 * 3
    for a in range(3):
        for b in range(3):
            if num == board[x + a][y + b]:
                return False

    return True


def dfs(depth):
    if depth == len(blank):
        for i in range(9):
            print(' '.join(map(str, board[i])))
        sys.exit()

    for i in range(1, 10):
        nx, ny = blank[depth]
        if chk(nx, ny, i):
            board[nx][ny] = i
            dfs(depth + 1)
            board[nx][ny] = 0


#board = [list(map(int, read().split())) for _ in range(9)]
board = [[0, 0, 5, 4, 6, 9, 2, 7, 8],
[0, 0, 2,1,3,5,6,4,9],
[4,6,9,2,7,8,1,3,5],
[3,2,1,5,4,6,8,9,7],
[8,7,4,9,1,3,5,2,6],
[5,9,6,8,2,7,4,1,3],
[9,1,7,6,5,2,3,8,4],
[6,4,3,7,8,1,9,5,2],
[2,5,8,3,9,4,7,6,1]]
tp = [list(x) for x in zip(*board)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

dfs(0)
