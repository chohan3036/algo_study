import bisect


def make_group():
    for i in range(4):
        for 



def solution(infos, queries):
    ans = []
    candidates = {}

    for info in infos:
        a, b, c, d, score = info.split(' ')
        cur_info = ''.join([a, b, c, d])
        if cur_info not in candidates:
            candidates[cur_info] = []
        candidates[cur_info].append(int(score))

    for query in queries:
        a, b, c, d_score = query.split(' and ')
        d, score = d_score.split(' ')

        if a == '-':
            a = ['cpp', 'java', 'python']
        else:
            a = [a]
        if b == '-':
            b = ['frontend', 'backend']
        else:
            b = [b]
        if c == '-':
            c = ['junior', 'senior']
        else:
            c = [c]
        if d == '-':
            d = ['chicken', 'pizza']
        else:
            d = [d]

        cur_queries = []
        for lang in a:
            for stack in b:
                for career in c:
                    for food in d:
                        cur_queries.append(''.join([lang, stack, career, food]))

        cur_selected = 0
        for cur_query in cur_queries:
            if cur_query in candidates:
                cur_selected += bisect.bisect_left(candidates, int(score))

        ans.append(cur_selected)

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
