import sys
read = lambda: sys.stdin.readline().strip()


def update(idx):
    while idx <= n:
        tree[idx] += 1
        idx += (idx & -idx)


def sum(start, end):
    if end < start:
        return 0
    result = 0
    idx = end
    while idx > 0:
        result += tree[idx]
        idx -= (idx & -idx)
    idx = start - 1
    while idx > 0:
        result -= tree[idx]
        idx -= (idx & -idx)
    return result


n = int(read())
a = list(map(int, read().split()))
a = sorted(enumerate(a), key=lambda x: (-x[1], x[0]))

tree = [0] * (n + 1)
ans = 0
for i in range(n):
    ans += sum(a[i][0], n)
    update(a[i][0] + 1)

print(ans)
