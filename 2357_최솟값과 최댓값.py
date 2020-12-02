import sys
read = lambda: sys.stdin.readline().strip()


def init_min(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = min(init_min(node * 2, start, mid),
                         init_min(node * 2 + 1, mid + 1, end))
        return tree[node]


def find_min(node, left, right):
    if left <= tree[node] <= right:
        return tree[node]

    else:
        return tree[node]



n, m = map(int, read().split())
num = [int(read()) for _ in range(n)]

inter = [tuple(map(int, read().split())) for _ in range(m)]
tree = [0] * (n * 3)
init_min(1, 0, n - 1)
print(tree)