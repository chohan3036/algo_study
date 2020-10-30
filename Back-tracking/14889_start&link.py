def go(index, first, second):
    # 탈출 조건 : 주어진 n명 모두 분배했으면
    if index == n:
        # 반씩 분배 안 됐으면 -1 반환
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff

    # 반 보다 많이 배정되면
    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1

    ans = -1
    t1 = go(index + 1, first + [index], second)     # 함수 호출할 때 + 연산자로 추가했던 팀원은
    if ans == -1 or (t1 != -1 and ans > t1):        # 함수 리턴하고 나면 자동으로 빼짐
        ans = t1                                    # ans != -1이라는 것은 위에서 배정된 값 없다는 것
    t2 = go(index + 1, first, second + [index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans      # 위에서 반씩 배정이 끝난 경우


n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0, [], []))