import sys
read = lambda: sys.stdin.readline().strip()


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = Node(node)

        parent = self.root
        # 루트보다 작을 경우
        while node < parent.data:
            if parent.left:
                parent = parent.left
            else:
                parent.left = Node(node)
                break

        # 루트보다 클 경우
        while node > parent.data:
            if parent.right:
                parent = parent.right
            else:
                parent.right = Node(node)
                break

    def search(self, node):
        result = []
        while True:
            while node:
                if node.right:
                    result.append(node.right)
                result.append(node)
                node = node.left
            node = result.pop()


nodes = []
while True:
    input_node = read()
    if not input_node:
        break
    nodes.append(int(input_node))

bst = BinarySearchTree()
for node in nodes:
    bst.insert(node)

bst.search(bst.root)
