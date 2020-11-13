import sys
read = lambda: sys.stdin.readline().strip()


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = Node(None)
        self.right = Node(None)


class BinarySearchTree(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, node):
        if not self.root.data:
            self.root.data = node

        parent = self.root
        # 루트보다 작을 경우
        while node < parent.data:
            if parent.left.data:
                parent = parent.left
            else:
                parent.left = Node(node)
                break

        # 루트보다 클 경우
        while node > parent.data:
            if parent.right.data:
                parent = parent.right
            else:
                parent.right = Node(node)
                break


nodes = []
while True:
    cur_node = read()
    if not cur_node:
        break
    nodes.append(int(cur_node))

bst = BinarySearchTree()
for node in nodes:
    bst.insert(node)

print(bst.root.left.left.data)
