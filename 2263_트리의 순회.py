import sys
sys.setrecursionlimit(10**6)
read = lambda: sys.stdin.readline().strip()

n = int(read())
in_order = list(map(int, read().split()))
post_order = list(map(int, read().split()))

order = [0] * (n + 1)
for i in range(n):
    order[in_order[i]] = i


def divide(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    parent = post_order[post_end]
    print(parent, end=' ')

    left = order[parent] - in_start
    right = in_end - order[parent]

    divide(in_start, in_start + left - 1, post_start, post_start + left - 1)
    divide(in_end - right + 1, in_end, post_end - right, post_end - 1)


divide(0, n - 1, 0, n - 1)
