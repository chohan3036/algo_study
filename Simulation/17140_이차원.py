from collections import Counter


def oper_r(idx_r):
    global nr, nc

    # R연산
    counter = Counter(board[idx_r])
    counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    sorted_r = []
    for c in counter:
        if c[0] == 0:
            continue
        sorted_r.append(c[0])
        sorted_r.append(c[1])
    sorted_r = sorted_r[:100]
    board[idx_r] = sorted_r

    # 만들어진 행이 현재 열의 길이보다 길면
    if len(sorted_r) > nc:
        for i in range(nr):
            if i == idx_r:
                continue
            board[i] += [0 for _ in range(len(sorted_r) - nc)]
        nc = len(sorted_r)
    else:
        for i in range(nr):
            board[idx_r][nc:] = [0 for _ in range(nc - len(sorted_r))]


def oper_c(idx_c):
    global nc, nr

    # C연산
    tmp_c = []
    for i in range(nr):
        tmp_c.append(board[i][idx_c])

    counter = Counter(tmp_c)
    counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    sorted_c = []
    for x in counter:
        if x[0] == 0:
            continue
        sorted_c.append(x[0])
        sorted_c.append(x[1])
    sorted_c = sorted_c[:100]

    # 만들어진 열이 현재 행의 길이보다 길면
    if len(sorted_c) > nr:
        for _ in range(len(sorted_c) - nr):
            board.append([0 for _ in range(nc)])
        nr = len(sorted_c)

    for i in range(nr):
        if i >= len(sorted_c):
            board[i][idx_c] = 0
        else:
            board[i][idx_c] = sorted_c[i]


r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
time = 0
nr, nc = 3, 3

while time <= 100:
    if r < nr and c < nc and board[r - 1][c - 1] == k:
        break

    time += 1

    if nr >= nc:
        for i in range(nr):
            oper_r(i)
    else:
        for i in range(nc):
            oper_c(i)

print(time if time <= 100 else -1)
