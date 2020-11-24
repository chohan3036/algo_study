import sys
read = lambda: sys.stdin.readline().strip()


def dfs(depth, result):
    global max_, min_

    if depth >= n - 1:
        max_ = max(max_, result)
        min_ = min(min_, result)
        return

    for i in range(4):
        if opd[i] > 0:
            result = int(eval(str(result) + opd_char[i] + str(opt[depth + 1])))
            opd[i] -= 1
            dfs(depth + 1, result)
            result = int(eval(str(result) + opd_char[i - 2] + str(opt[depth + 1])))
            opd[i] += 1


n = int(read())
opt = list(map(int, read().split()))
opd = list(map(int, read().split()))
opd[1], opd[2] = opd[2], opd[1]
opd_char = ['+', '*', '-', '/']
max_, min_ = -1000000000, sys.maxsize
dfs(0, opt[0])
print(max_)
print(min_)
