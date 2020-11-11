import sys
read = lambda: sys.stdin.readline().strip()


def dc(x, y, size):
    cur_paper = origin[x][y]
    if size == 1:
        papers[cur_paper] += 1
        return

    for i in range(x, x + size):
        for j in range(y, y + size):
            if origin[i][j] != cur_paper:
                size //= 3
                for k in range(9):
                    dc(x + k // 3 * size, y + k % 3 * size, size)
                return

    papers[cur_paper] += 1


n = int(read())
papers = {-1: 0, 0: 0, 1: 0}
origin = [list(map(int, read().split())) for _ in range(n)]

dc(0, 0, n)
print(papers[-1])
print(papers[0])
print(papers[1])
