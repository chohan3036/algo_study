from collections import deque as dq


def solution(tickets):
    ans = []

    sights = dict()
    for ticket in tickets:
        stt, end = ticket
        if stt not in sights:
            sights[stt] = set()
        sights[stt].add(end)

    q = dq(['ICN'])
    visited = set()
    while q:
        cur_stt = q.popleft()
        for pss_city in sights[cur_stt][-3:]:

    return ans


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
