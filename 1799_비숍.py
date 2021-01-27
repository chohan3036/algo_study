import sys
read = lambda: sys.stdin.readline().strip()


def dfs(x, y, cnt):
    return


n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]
ans = 0
left, right = [], []

