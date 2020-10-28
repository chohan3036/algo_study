# 시간초과.. 해시를 써야할 것 같은데
# 트라이를 구현하는 문제!!
# node가 dictinary에 들어가는구나.. 그래도 검색이 됨
'''
import re
import sys
read = lambda: sys.stdin.readline().strip()


def solution(words, queries):
    ans = [0] * len(queries)
    idx = 0
    for q in queries:
        re_q = q.replace('?', '.')
        for w in words:
            if re.fullmatch(re_q, w):
                ans[idx] += 1
        idx += 1
    return ans
'''
from collections import deque

# 문자를 담을 노드
class Node(object):
    def __init__(self, key, data=None):
        self.key = key      # 단어 중에 글자 하나
        self.data = data    # 단어의 끝인지 알려주는 flag
        self.children = {}  # 다음 단어


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열을 삽입
    def insert(self, string):
        cur_node = self.head
        for char in string:
            # 해당 문자를 자식 트리에서 검색
            # 해당 문자가 없으면 Node 새로 생성하여 저장
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)

            # 자식 트리로 이어줌
            cur_node = cur_node.children[char]

        # 문자열의 마지막 글자면,
        # Node 의 data 에 저장하려는 문자열 전체를 저장
        cur_node.data = string

    def search(self, string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False

        # 문자열의 마지막에 도달했는데
        # cur_node 에 data 가 있다면 해당 문자열이 Trie 에 존재하는 것!
        if cur_node.data is not None:
            return True

    # 접두사로 시작하는 모든 문자열 찾기
    # 이 문제에서는 와일드카드 갯수를 제한으로 둬야 할듯!
    def starts_with(self, prefix, wild_cnt):
        cur_node = self.head
        result = []
        subtrie = None

        # Trie 에서 prefix 를 찾고,
        # prefix 의 마지막 글자 노드를 subtire 로 설정
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                subtrie = cur_node
            else:
                return None

        # bfs 로 prefix subtrie 를 순회하며
        # data 가 있는 Node 들(=완전한 문자열)을 찾는다
        queue = deque([subtrie.children.value()])
        while queue:
            cur = queue.popleft()
            if cur.data is not None:
                result.append(cur.data)
            queue.append(list(cur.children.value()))

        return len(result)


def solution(words, queries):
    ans = []
    ord_trie, rvs_trie = Trie(), Trie()
    for w in words:
        ord_trie.insert(w)
        rvs_trie.insert(w[::-1])

    for q in queries:
        print()
    return ans


if __name__ == '__main__':
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                   ["fro??", "????o", "fr???", "fro???", "pro?"]))