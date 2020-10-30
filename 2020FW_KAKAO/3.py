# 트리?


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        # 자식 트리를 딕셔너리로 관리함
        self.children = {}


class Tree(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, person):
        # 사람 한 명씩 볼 때마다 헤드부터 시작!
        cur_node = self.head

        # 이 사람에 대한 조건을 차례로 봄
        for detail in person:
            # 코딩 점수는 마지막 노드를 의미
            # 몇 점 이상, 즉 노드 개수 세야 해서 마지막 노드는 무조건 생성
            if detail.isdigit():
                cur_node.data = int(detail)
            else:
                # 다른 정보의 경우 정해져 있으므로..
                # 해당 조건의 자식 트리를 찾아감
                if detail not in cur_node.children:
                    cur_node.children[detail] = Node(detail)
                cur_node = cur_node.children[detail]

    def search(self, query):
        cur_node = self.head
        result = []
        subtree = None

        for detail in query:
            if detail in cur_node.children:
                cur_node = cur_node.children[detail]
                subtree = cur_node
            else:
                return None


        return result


def solution(info, query):
    info = [x.split() for x in info]
    query = [x.split for x in query]

    answer = []
    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],

               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))
