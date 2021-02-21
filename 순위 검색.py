from bisect import bisect_left
from itertools import combinations


def solution(infos, queries):
    ans = []
    candidates = {}

    for info in infos:
        a, b, c, d, score = info.split(' ')
        for i in range(5):
            combination = combinations([0, 1, 2, 3], i)
            for _pos in combination:
                temp = [a, b, c, d]
                for cur_pos in _pos:
                    temp[cur_pos] = '-'
                new_info = ''.join(temp)
                if new_info not in candidates:
                    candidates[new_info] = []
                candidates[new_info].append(int(score))

    for key in candidates.keys():
        candidates[key].sort()

    for query in queries:
        a, b, c, d = query.split(' and ')
        d, score = d.split(' ')
        new_query = ''.join([a, b, c, d])
        if new_query not in candidates:
            ans.append(0)
        else:
            array = candidates[new_query]
            size = len(array)
            cnt = bisect_left(array, int(score))
            ans.append(size - cnt)

    return ans


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
