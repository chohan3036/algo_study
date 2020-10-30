def go(start, end, cur_cost, costs):
    if start == end:    # 진열이 완벽하게 바뀌면 현재 비용을 리스트에 추가
        costs.append(cur_cost)
        return

    s, cc = start, cur_cost
    for c in cost:
        if s == c[0][0]:    # 현재 start와 같은 진열이 있으면
            s = c[0][1]     # 그 진열의 다음 진열로 start 바꾸기
            cc += c[1]      # 비용 더해주기
            go(s, end, cc, costs)   # 이 상태로 dfs
            s = start       # 다 돌고나면 다시 되돌려주기
            cc = cur_cost

    return costs    # 비용들을 저장한 리스트 return


n, m = map(int, input().split())
cost = []
for _ in range(m):
    s1, s2, c = map(str, input().split())
    c = int(c)
    cost.append([(s1, s2), c])

question = []
for _ in range(int(input())):
    q1, q2 = map(str, input().split())
    if q1 == q2:    # 진열을 안 바꿔도 되면 바로 0 출력
        print(0)
    else:           # 그렇지 않을 때는 dfs 시작
        result = go(q1, q2, 0, [])
        if result:  # 반환된 리스트가 비어있지 않으면 최솟값 출력
            print(min(result))
        else:       # 반환된 리슽트가 비어있으면 -1 출력
            print(-1)
