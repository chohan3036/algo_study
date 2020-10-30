from collections import deque
from copy import deepcopy


def solution(depar, hub, dest, roads):
    graph = dict()
    for n1, n2 in roads:
        if n1 in graph:
            graph[n1].add(n2)
        else:
            graph[n1] = set()
            graph[n1].add(n2)

    hub_q = deque([[depar]])
    hub_road = []
    while hub_q:
        cur_city = hub_q.popleft()
        for next_city in graph[cur_city[-1]]:
            if next_city == dest:
                continue
            cur_cities = deepcopy(cur_city)
            if next_city == hub:
                cur_cities.append(next_city)
                hub_road.append(cur_cities)
            else:
                cur_cities.append(next_city)
                hub_q.append(cur_cities)

    dest_q = deque([[hub]])
    dest_road = []
    while dest_q:
        cur_city = dest_q.popleft()
        for next_city in graph[cur_city[-1]]:
            cur_cities = deepcopy(cur_city)
            if next_city == dest:
                cur_cities.append(next_city)
                dest_road.append(cur_cities)
            else:
                cur_cities.append(next_city)
                dest_q.append(cur_cities)

    return len(hub_road) * len(dest_road)


print(solution("SEOUL", "DAEGU", "YEOSU",
               [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],
                ["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],
                ["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],
                ["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]))
