import sys
read = lambda: sys.stdin.readline().strip()


def init_tree(node, start, end):
    if start == end:
        tree[node] = a[node]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init_tree(node * 2, start, mid)


n = int(read())
a = list(map(int, read().split()))

tree = [0] * n

