import sys
read = lambda: sys.stdin.readline().strip()


def dc(x, y, size):
    cur_paper = origin[x][y]
    flag = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if origin[i][j] != cur_paper:
                flag = False
                break
        if not flag:
            break

    if flag:
        papers[cur_paper] += 1

    else:
        size //= 3
        dc(x, y, size)
        dc(x + size, y, size)
        dc(x + 2 * size, y, size)
        dc(x, y + size, size)
        dc(x, y + 2 * size, size)
        dc(x + size, y + size, size)
        dc(x + 2 * size, y + 2 * size, size)


n = int(read())
papers = {-1: 0, 0: 0, 1: 0}
origin = [list(map(int, read().split())) for _ in range(n)]

dc(0, 0, 9)
print(papers)