import sys
read = lambda: sys.stdin.readline().strip()

n, m = map(int, read().split())
num = [int(read()) for _ in range(n)]
inter = [tuple(map(int, read().split())) for _ in range(m)]

mins = [[0 for _ in range(n)] for _ in range(n)]
maxs = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if j == 0:
            mins[i][j], maxs[i][j] = num[i], num[i]
            continue
        mins[i][j] = min(mins[i][j - 1], num[j])
        maxs[i][j] = max(maxs[i][j - 1], num[j])

print(mins)
print(maxs)

for a, b in inter:
    a_idx, b_idx = num.index(a), num.index(b)
    print(mins[a_idx][b_idx], ' ', maxs[a_idx][b_idx])
