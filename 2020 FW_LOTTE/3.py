def solution(p, index):
    ans = ''
    top = p * index # index번째 수가 포함되는 대략적인 범위

    for i in range(top):
        cur_num = ''

        # i가 p보다 같거나 크면
        # p로 나눈 나머지를 cur_num 앞에 붙여줌
        while i >= p:
            cur_num = str(i % p) + cur_num
            i //= p

        # 나머지가 p보다 작아지면
        # cur_num 앞에 붙여줌
        cur_num = str(i) + cur_num

        # p진법으로 변환된 i를 ans에 붙여줌
        ans += cur_num

    # 문자열로 구성된 ans에서 index번째 수를 읽음
    return int(ans[index - 1])