import sys
read = lambda: sys.stdin.readline().strip()


def init_min(node, start, end):
    if start == end:
        tree_min[node] = num[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(init_min(node * 2, start, mid),
                         init_min(node * 2 + 1, mid + 1, end))
    return tree_min[node]


def init_max(node, start, end):
    if start == end:
        tree_max[node] = num[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(init_max(node * 2, start, mid),
                         init_max(node * 2 + 1, mid + 1, end))
    return tree_max[node]


def find_min(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(find_min(node * 2, start, mid, left, right),
               find_min(node * 2 + 1, mid + 1, end, left, right))


def find_max(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(find_max(node * 2, start, mid, left, right),
               find_max(node * 2 + 1, mid + 1, end, left, right))


n, m = map(int, read().split())
num = [int(read()) for _ in range(n)]
tree_min, tree_max = [0] * (n * 4), [0] * (n * 4)
init_min(1, 0, n - 1)
init_max(1, 0, n - 1)
inter = [tuple(map(int, read().split())) for _ in range(m)]

for a, b in inter:
    print(find_min(1, 0, n - 1, a - 1, b - 1), end=' ')
    print(find_max(1, 0, n - 1, a - 1, b - 1))
