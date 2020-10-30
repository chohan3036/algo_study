class Node(object):
    def __init__(self, data):
        self.data = data
        self.child = {}


class Tree(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, edges):
        cur_node = self.head
        for n1, n2 in edges:
            if n1 not in cur_node.child:
                cur_node.child[n1] = Node(n1)
            if n2 not in n1.child:
                n1.child[n2] = Node(n2)


def solution(n, edges):
    ans = 0

    return ans

