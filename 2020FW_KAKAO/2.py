# 시간초과 날 것 같음

from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    ans = set()
    combi_dic = {}
    # 조합을 저장할 딕셔너리
    for course_num in course:
        combi_dic[course_num] = set()
        course_dic = defaultdict(int)

        for order in orders:
            # 각 주문에서 나올 수 있는 조합
            order_combi = list(combinations(order, course_num))
            combi_dic[course_num].update(set(order_combi))

        print(combi_dic)

        for order in orders:
            # 조합을 순회하며 딕셔너리에 있는지 검사
            # 없으면 1로 초기화, 있으면 1을 더해줌
            for combi in combi_dic[course_num]:
                if (set(combi) & set(order)) == set(combi):
                    course_dic[combi] += 1

        print(course_dic)

        # 최대값이 여러 개일 가능성 고려
        if course_dic:
            max_cnt = max(course_dic.values())
            if max_cnt < 2:
                continue
            else:
                for k, v in course_dic.items():
                    if v == max_cnt:
                        ans.add(k)

    ans_set = set()
    for a in ans:
        ans_set.add(''.join(sorted(a)))

    return sorted(ans_set)


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
