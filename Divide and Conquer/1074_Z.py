import sys

n, r, c = map(int, input().split())
board = [[0 for _ in range(2 ** n)]]

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
b = []


def solve(n, x, y, a):
    if n == 2:
        for i in range(4):
            if (x + dx[i], y + dy[i]) == (r, c):
                b.append(a)
                print(sum(b))
                sys.exit(1)
            else:
                a += 1
        return b.append(a)

    solve(n/2, x, y, a)
    solve(n/2, x, y + n / 2, a)
    solve(n/2, x + n / 2, y, a)
    solve(n/2, x + n / 2, y + n / 2, a)


solve(2 ** n, 0, 0, 0)
