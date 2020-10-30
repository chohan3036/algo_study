def solution(k, scores):
    cnt = dict()
    hacked = dict()
    for i in range(1, len(scores)):
        diff = scores[i - 1] - scores[i]
        if diff in cnt:
            cnt[diff] += 1
        else:
            cnt[diff] = 1
            hacked[diff] = set()
        hacked[diff].add(scores[i - 1])
        hacked[diff].add(scores[i])

    ans = set()
    for key in cnt:
        if cnt[key] >= k:
            ans |= hacked[key]

    return len(scores) - len(ans)


print(solution(2, [1300000000, 700000000, 668239490, 618239490, 568239490, 568239486, 518239486, 157658638, 157658634,
                   100000000, 100]))
