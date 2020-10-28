from copy import deepcopy
import re

visit = []


def dfs(cur_banned_user, case, depth):
    if depth >= len(cur_banned_user):
        if case not in visit:
            visit.append(deepcopy(case))
        return

    for a in cur_banned_user[depth]:
        if a not in case:
            case.add(a)
            dfs(cur_banned_user, case, depth + 1)
            case.remove(a)


def solution(user_id, banned_id):
    cur_banned_user = []
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*', '.')
        banned_user = set()
        for id in user_id:
            if re.fullmatch(banned_id[i], id):
                banned_user.add(id)
        cur_banned_user.append(banned_user)

    dfs(cur_banned_user, set(), 0)
    return len(visit)


if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                   ["fr*d*", "*rodo", "******", "******"]))