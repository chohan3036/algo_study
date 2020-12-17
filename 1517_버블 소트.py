import sys
read = lambda: sys.stdin.readline().strip()


def intersum(node, start, end, left, right):
    if right < start or left > end:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return intersum(node * 2, start, mid, left, right) + intersum(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index):
    if index < start or end < index:
        return tree[node]

    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    tree[node] = update(node * 2, start, mid, index) + update(node * 2 + 1, mid + 1, end, index)
    return tree[node]


n = int(read())
a = list(map(int, read().split()))
a = sorted(enumerate(a), key=lambda x: (-x[1], -x[0]))

tree = [0] * (n * 4)
ans = 0
for i in range(n):
    ans += intersum(1, 0, n - 1, 0, a[i][0])
    update(1, 0, n - 1, a[i][0])

print(ans)
