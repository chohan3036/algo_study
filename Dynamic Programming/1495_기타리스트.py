import sys
read = lambda: sys.stdin.readline().strip()

n, s, m = map(int, read().split())
v = [0] + list(map(int, read().split()))

d = [[0] * (m + 1) for _ in range(n + 1)]
d[0][s] = 1
for i in range(n):
    for j in range(m + 1):
        if d[i][j] == 0:
            continue

        if j + v[i + 1] <= m:
            d[i + 1][j + v[i + 1]] = 1

        if j - v[i + 1] >= 0:
            d[i + 1][j - v[i + 1]] = 1

ans = -1
for i in range(m, -1, -1):
    if d[n][i] == 1:
        ans = i
        break

print(ans)
