from itertools import combinations
from collections import Counter


def solution(orders, course):
    ans = []
    for i in course:
        all_menus = dict()
        for order in orders:
            menus = combinations(order, i)
            for menu in menus:
                menu = ''.join(sorted(menu))
                if menu not in all_menus:
                    all_menus[menu] = 1
                else:
                    all_menus[menu] += 1

        candidates = Counter(all_menus).most_common()
        ans += [menu for menu, cnt in candidates if cnt > 1 and cnt == candidates[0][1]]

    return sorted(ans)


print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
