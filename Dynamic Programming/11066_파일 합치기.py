import sys
read = lambda: sys.stdin.readline().strip()


def go(i, j):
    if i == j:
        return 0

    if d[i][j] != -1:
        return d[i][j]

    ans = -1
    cost = sum(novel[i: j + 1])
    for k in range(i, j):
        temp = go(i, k) + go(k + 1, j) + cost
        if ans == -1 or ans > temp:
            ans = temp

    d[i][j] = ans
    return ans


t = int(read())
for _ in range(t):
    k = int(read())
    novel = list(map(int, read().split()))

    d = [[-1] * k for _ in range(k)]
    print(go(0, k - 1))
