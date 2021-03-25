def solution(data, word):
    graph = dict()
    node = dict()
    for d in data:
        id, name, parent_id = d.split(' ')
        if parent_id not in graph:
            graph[parent_id] = []
        if id not in graph:
            graph[id] = []
        graph[parent_id].append(id)
        node[id] = name

    return graph


print(solution(["1 BROWN 0",
                "2 CONY 0",
                "3 DOLL 1",
                "4 DOLL 2",
                "5 LARGE-BROWN 3",
                "6 SMALL-BROWN 3",
                "7 BLACK-CONY 4",
                "8 BROWN-CONY 4"],
               "BROWN"))