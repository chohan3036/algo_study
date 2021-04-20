def solution(enroll, referral, seller, amount):
    children = {'center': set()}
    parents = dict()
    interests = {'center': 0}

    for child, parent in zip(enroll, referral):
        if parent == '-':
            children['center'].add(child)       # 아랫 사람 저장
            parents[child] = 'center'           # 추천인 저장
            interests[child] = 0
        else:
            if parent not in children:
                children[parent] = set()
            children[parent].add(child)
            parents[child] = parent
            interests[child] = 0

    for s, a in zip(seller, amount):
        a *= 100
        interests[s] += round(a * 0.9)
        while parents[s]:
            a -= round(a * 0.9)
            if parents[s] == 'center':
                interests[parents[s]] += a
                break
            else:
                interests[parents[s]] += round(a * 0.9)
                s = parents[s]

    ans = []
    for e in enroll:
        ans.append(int(interests[e]))

    return ans


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
