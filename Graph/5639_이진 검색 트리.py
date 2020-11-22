import sys
read = lambda: sys.stdin.readline().strip()

tree = []
while True:
    cur_node = read()
    if not cur_node:
        break
    tree.append(int(cur_node))


def bst(part, node, bound):
    right = node + 1
    while right <= bound and part[right] < part[node]:
        right += 1

    left = node + 1
    if left <= right - 1:
        bst(part, left, right - 1)

    if right <= bound:
        bst(part, right, bound)

    print(part[node])


bst(tree, 0, tree[0])
