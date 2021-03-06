import sys
read = lambda: sys.stdin.readline().strip()

mod = 1000000007


def init(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node] % mod

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)
    return tree[node] % mod


def find(node, start, end, left, right):
    if start > right or end < left:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (find(node * 2, start, mid, left, right) * find(node * 2 + 1, mid + 1, end, left, right)) % mod


def change(node, start, end, index, target):
    if index < start or end < index:
        return tree[node]

    if start == end:
        tree[node] = target
        return tree[node]

    mid = (start + end) // 2
    tree[node] = change(node * 2, start, mid, index, target) * change(node * 2 + 1, mid + 1, end, index, target)
    return tree[node] % mod


n, m, k = map(int, read().split())
num = [int(read()) for _ in range(n)]
tree = [0] * (n * 4)
init(1, 0, n - 1)

ans = []
for _ in range(m + k):
    a, b, c = map(int, read().split())
    if a == 1:
        change(1, 0, n - 1, b - 1, c)
    else:
        ans.append(find(1, 0, n - 1, b - 1, c - 1))

for a in ans:
    print(a)
