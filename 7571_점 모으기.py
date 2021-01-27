import sys
read = lambda: sys.stdin.readline().strip()

n, m = map(int, read().split())
x, y = [], []
for _ in range(m):
    i, j = map(int, read().split())
    x.append(i)
    y.append(j)
x.sort()
y.sort()

mid_x, mid_y = x[m // 2], y[m // 2]

ans = 0
for i, j in zip(x, y):
    ans += abs(mid_x - i) + abs(mid_y - j)

print(ans)
